import semver
import logging
import urlparse
import requests
import json
import os
import sys

GITHUB_RAW = 'https://api.github.com/repos'
GITHUB_ORG = 'carbon-io'
SCOPE = '@carbon-io/'

def strip_scope(name):
    return name.replace(SCOPE,'')

def add_scope(name):
    return SCOPE + name

def build_uri_for_github_tag_api(package):
    return "/repos/" + GITHUB_ORG + "/" + package + "/git/refs/tags"

def find_latest_matching_tag_for_package(package_name, semver_range):
    refs = fetch(build_uri_for_github_tag_api(package_name))
    tags = []
    latest_matching_tag = None
    for ref in refs:
        tag = ref['ref'].replace('refs/tags/v','')
        if desugar_range_and_match(tag, semver_range):
            latest_matching_tag = tag
        tags.append(ref['ref'].replace('refs/tags/v',''))
    return latest_matching_tag

# assumes use of 'x', following npm docs at
# https://docs.npmjs.com/getting-started/semantic-versioning
def desugar_range_and_match(version, semver_range):
    if 'x' in semver_range:
        if len(semver_range.split('.')) < 3:
            range_floor = semver_range.replace('x', '0.0')
            range_ceiling = semver.bump_major(range_floor)
        else:
            range_floor = semver_range.replace('x','0')
            range_ceiling = semver.bump_minor(range_floor)

    if not semver.match(version, ">="+range_floor):
        return False
    if not semver.match(version, "<"+range_ceiling):
        return False
    return True

def compare_submodule_versions_to_latest(action_on_mismatch=None):
    os.chdir('../docs/packages')
    for (dirpath,_,_) in os.walk('.'):
        if os.path.exists(dirpath + '/package.json') and 'node_modules' not in dirpath:
            with open(dirpath + '/package.json') as package:
                package_json = json.load(package)
                name = strip_scope(package_json['name'])
                version = package_json['version']
                parent = dirpath[:-(len('/docs/packages/' + name)-1)]
                if parent:
                    with open(parent + '/package.json') as parent_package:
                        parent_package_json = json.load(parent_package)
                        parent_name = parent_package_json['name']
                        latest_matching_tag = find_latest_matching_tag_for_package(name, parent_package_json['dependencies'][add_scope(name)])
                        logging.info("module: %s" % name)
                        logging.info("parent: %s" % strip_scope(parent_name))
                        logging.info("dependency semver -> %s" % (parent_package_json['dependencies'][add_scope(name)]))
                        logging.info("latest matching tag: %s" % (latest_matching_tag))
                        logging.info("current version: %s\n" % version)
                        if version != latest_matching_tag:
                            logging.info("***Current version does not match latest tag***")
                            if action_on_mismatch:
                                action_on_mismatch(latest_matching_tag, path)

def fetch(uri, cache=None):
    parts = urlparse.urlparse(urlparse.urljoin(GITHUB_RAW, uri))
    if parts.scheme in ['http', 'https']:
        uri = urlparse.urlunparse(parts)
        cache_path = None if cache is None \
                          else os.path.join(cache, uri.replace('/', '_'))
        if cache_path is not None and \
           os.path.exists(cache_path):
            return json.loads(open(cache_path).read())
        logging.info('fetching %s', uri)
        req = requests.get(uri)
        data = req.json()
        if cache_path is not None:
            open(cache_path, 'w').write(json.dumps(data, indent=4,
                                                   sort_keys=True))
        return data
    else:
        raise Exception('{!s} is not a suppported scheme'.format(parts.scheme))
