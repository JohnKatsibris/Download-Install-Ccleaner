import urllib
import os

def main(URL='https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE/cookie_mmm_ccl_003_999_a6a_m', sCMD='/S'):
    Path=os.environ['PROGRAMFILES']
    if os.path.exists(Path):
        fn = URL.split('/')[-1]
        fp = os.path.join(Path, fn)
        try:
            with open(fp, 'wb') as f:
                try:
                    f.write(urllib.urlopen(URL).read())
                    print fp
                except Exception as e:
                    print e
        except Exception as e:
            print e
        try:
            os.popen(fp+' '+sCMD).read()
            Path=os.environ['PROGRAMFILES']+'\\ccsetup523.exe'
            os.remove(Path)
            return 'Great! Successfully Installed'
        except Exception as e:
            return e
    else:
        return 'No path: '+Path+' is exist'

print main()
