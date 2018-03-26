import semver
import subprocess
import logging
import urlparse
import urllib
import json
import shlex
import os
import sys

GITHUB_RAW = 'https://api.github.com/repos'
GITHUB_ORG = 'carbon-io'
SCOPE = '@carbon-io/'
PATH_BLACKLIST = [
    'node_modules',
    '.git',
    ['docs', '_build'],
    'code-frags'
]
SCRIPT_HOME = os.path.dirname(os.path.dirname(__file__))

def strip_scope(name):
    return name.replace(SCOPE,'')

def add_scope(name):
    return SCOPE + name

def build_uri_for_github_api(package):
    access_token = ''
    if "GITHUB_API_ACCESS" in os.environ:
        access_token = "/?access_token=" + os.environ["GITHUB_API_ACCESS"]
    else:
        logging.info("No access token found for github API: requests rate limited at 60 requests per hour.")
    return "/repos/" + GITHUB_ORG + "/" + package + "/git/refs/tags" + access_token

def find_latest_matching_tag_for_package(package_name, semver_range):
    refs = fetch(build_uri_for_github_api(package_name))
    latest_matching_tag = "0.0.0"
    for ref in refs:
        tag = ref['ref'].replace('refs/tags/v','')
        # must desugar advanced range syntax to use the semver library
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

def exists_in_submodule_path(dirpath):
    if not os.path.exists(dirpath):
        return False
    parts = dirpath.split(os.path.sep)
    for subpath in PATH_BLACKLIST:
        subpath = [subpath] if not isinstance(subpath, list) else subpath
        for i in xrange(len(parts)):
            match = True
            for j in xrange(len(subpath)):
                if i+j >= len(parts) or subpath[j] != parts[i+j]:
                    match = False
                    break
            if match:
                return False
    return True

def has_children(dirpath):
    # TODO: if /docs/packages exists, also check if it is empty
    if exists_in_submodule_path(os.path.join(dirpath, 'docs/packages')):
        return True
    else:
        return False

def do_checkout(dirpath, branch, merge=False, pull=False):
    cwd = os.getcwd()
    fetch_cmd = "git fetch"
    checkout_cmd = "git checkout %s" % branch
    # We only want to merge when we will be pushing to remote
    # i.e. when we are on master branch (parent module)
    if merge:
        merge_cmd = "git merge --no-edit origin %s"  % branch
    os.chdir(dirpath)
    subprocess.call(shlex.split(fetch_cmd))
    checkout_return_code = subprocess.call(shlex.split(checkout_cmd))
    # if checkout returns anything other than '0', switch to master (release branch doesn't exist)
    if checkout_return_code and merge:
        logging.info("Checking out branch %s FAILED, defaulting to master branch..." % branch)
        checkout_cmd = "git checkout master"
        subprocess.call(shlex.split(checkout_cmd))
    if merge:
        subprocess.call(shlex.split(merge_cmd))
    if pull:
        subprocess.call(shlex.split('git pull origin %s' % branch))
    os.chdir(cwd)

def get_target_remote_release_branch(dirpath, latest_matching_tag):
    parsed_tag = semver.parse(latest_matching_tag)
    constructed_release_branch = "v%s.%s" % (parsed_tag['major'], parsed_tag['minor'])
    return constructed_release_branch

def get_out_of_date_submodules(checkout=False):
    out_of_date_submodules = []
    for (dirpath,_,_) in os.walk(os.path.abspath(os.path.join(SCRIPT_HOME, '..'))):
        if exists_in_submodule_path(os.path.join(dirpath, 'package.json')):
            with open(os.path.join(dirpath, 'package.json')) as package:
                package_json = json.load(package)
                name = strip_scope(package_json['name'])
                version = package_json['version']
                parent = dirpath[:dirpath.rfind('/docs/packages/')+1]
                if parent:
                    with open(os.path.join(parent, 'package.json')) as parent_package:
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
                            if semver.compare(latest_matching_tag, version) == -1:
                                raise RuntimeError("The current version of %s (%s) succeeds the latest matching tag (%s)!!! The submodule tree requires manual intervention" % (name, version, latest_matching_tag))

                            out_of_date_submodules.append({"path" : dirpath,
                                                           "parent_path" : parent})
                            if checkout:
                                if has_children(dirpath):
                                    # parent node, will be tagging so fetch and checkout master
                                    release_branch = get_target_remote_release_branch(dirpath, latest_matching_tag)
                                    logging.info("Checking out %s branch for %s...\n" % (release_branch, name))
                                    logging.info("LATEST MATCHING TAG: %s" % latest_matching_tag)
                                    do_checkout(dirpath, release_branch, merge=True)
                                else:
                                    # leaf node, fetch and checkout latest_matching_tag
                                    logging.info("Checking out latest matching tag (%s) for %s...\n" % (latest_matching_tag, name))
                                    do_checkout(dirpath, "v" + latest_matching_tag)


    return out_of_date_submodules

def build_parent_submodule_update_order(deepest_depth):
    parent_submodules = {}
    for (dirpath,_,_) in os.walk('..'):
        if has_children(dirpath):
            depth = dirpath.count('docs/packages')
            if depth <= deepest_depth:
                parent_submodules[dirpath] = depth
            # checkout in case this parent was not out of date
            do_checkout(dirpath, 'master', merge=True)
    parent_submodules = sorted(parent_submodules, key=parent_submodules.get, reverse=True)
    return parent_submodules

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

