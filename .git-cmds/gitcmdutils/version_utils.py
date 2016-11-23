import semver
import logging
import urlparse
import urllib
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
    latest_matching_tag = "0.0.0"
    for ref in refs:
        tag = ref['ref'].replace('refs/tags/v','')
        if desugar_range_and_match(tag, semver_range):
            if semver.compare(tag, latest_matching_tag) == 1:
                latest_matching_tag = tag
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

def log_info(package_name, parent, dep_semver, latest_matching_tag, current_version):
    logging.info("module: %s" % package_name)
    logging.info("parent: %s" % parent)
    logging.info("dependency semver: %s" % dep_semver)
    logging.info("latest matching tag: %s" % latest_matching_tag)
    logging.info("current version: %s\n" % current_version)

def get_out_of_date_submodules():
    out_of_date_submodules = []
    for (dirpath,_,_) in os.walk('..'):
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
                        parent_dependencies = parent_package_json['dependencies']
                        latest_matching_tag = \
                            find_latest_matching_tag_for_package(name, parent_dependencies[add_scope(name)])
                        log_info(name, 
                                 strip_scope(parent_name), 
                                 parent_dependencies[add_scope(name)], 
                                 latest_matching_tag, 
                                 version)
                        if version != latest_matching_tag:
                            out_of_date_submodules.append({"path" : dirpath,
                                                           "parent_path" : parent})
    return out_of_date_submodules

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
        req = urllib.urlopen(uri)
        data = json.loads(req.read())
        if cache_path is not None:
            open(cache_path, 'w').write(json.dumps(data, indent=4,
                                                   sort_keys=True))
        return data
    else:
        raise Exception('{!s} is not a suppported scheme'.format(parts.scheme))

