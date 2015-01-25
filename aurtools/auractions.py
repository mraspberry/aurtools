#!/usr/bin/env python
"""
This script searches the Arch Linux AUR for the provided package names and prints out all results returned

Author: Matthew Raspberry
Email: nixalot[at]nixalot[dot]com

Copyright 2013 Matthew Raspberry

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests
import tarfile
import tempfile

AURBASE = 'https://aur.archlinux.org'
_AURRPC = '{base}/rpc.php'.format(base=AURBASE)

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
