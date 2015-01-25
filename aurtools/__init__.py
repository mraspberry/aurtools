"""
Copyright (c) 2015, Matthew Raspberry
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    * Neither the name of aurtools nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import aurtools.auractions as actions
from argparse import ArgumentParser

AURBASE = 'https://aur.archlinux.org'

def _init_argparser():
    parser = ArgumentParser()
    parser.add_argument('packages',action='store',metavar='package',nargs='+',
            help="Package name to download")
    return parser.parse_args()

def aurdownload():
    args = _init_argparser()
    for pkgname in args.packages:
        tfile = actions.downloadPkg(pkgname)
        if not tfile:
            print("{} not found".format(pkgname))
            continue
        else:
            print("Extracting {} to current directory".format(pkgname))
        tfile.extractall()
        tfile.close()

def aursearch():
    args = _init_argparser()
    for pkgname in args.packages:
        results = actions.searchAur(pkgname)
        for res in results:
            print("    Name: {0}".format(res['Name']))
            print("    Version: {0}".format(res['Version']))
            print("    Maintainer: {0}".format(res['Maintainer']))
            print("    ID: {0}".format(res['ID']))
            print("    Out of Date: {0}".format(res['OutOfDate']))
            print("    License: {0}".format(res['License']))
            print("    URL: {0}".format(AURBASE + res['URLPath']))
            print("    Description: {0}".format(res['Description']),end='\n\n')
