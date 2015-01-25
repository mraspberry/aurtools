import requests
import tarfile
import tempfile

_AURBASE = 'https://aur.archlinux.org'
_AURRPC = '{base}/rpc.php'.format(base=_AURBASE)

def _get_results(resultobj):
    return resultobj.json()['results']

def searchAur(pkgname):
    """Searches the AUR for the given package name and returns the results"""
    urlparams = {'type' : 'search',
                 'arg' : pkgname,
                }
    results = requests.get(_AURRPC,params=urlparams,verify=True)
    return _get_results(results)

def downloadPkg(pkgname):
    """Downloads the requested package if it exists and returns a tarfile.Tarfile object"""
    results = searchAur(pkgname)
    for res in results:
        if res['Name'] == pkgname:
            url = '{base}/{path}'.format(base=_AURBASE,path=res['URLPath'])
            pkg = requests.get(url,verify=True)
            tmp = tempfile.TemporaryFile()
            tmp.write(pkg.content)
            tmp.flush()
            tfile = tarfile.TarFile(fileobj=tmp)
            return tfile
