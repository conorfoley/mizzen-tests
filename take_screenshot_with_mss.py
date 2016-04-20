from platform import system
import mss
mss_class = mss.MSSMac

def on_exists(fname):
        ''' Callback example when we try to overwrite an existing
            screenshot.
        '''
        from os import rename
        from os.path import isfile
        if isfile(fname):
            newfile = 'old-' + fname
            print('{0} -> {1}'.format(fname, newfile))
            rename(fname, newfile)
        return True

def takeScreenshot(outputFileName='mss-screenshot.png'):

	
	mss = mss_class()

	for filename in mss.save(output=outputFileName, screen=1, callback=on_exists):
		print('File: "{0}" created.'.format(filename))

if __name__ == '__main__':
	takeScreenshot()