import codecs;
import sys;
import locale
 
def p(f):
    print '%s.%s(): %s' % (f.__module__, f.__name__, f())
 
p(sys.getdefaultencoding)
 
p(sys.getfilesystemencoding)
 
p(locale.getdefaultlocale)

p(locale.getpreferredencoding)

ustr = u'bbbbb\xe1';
print ustr;
print type(ustr);
astr = ustr.encode("ascii",'ignore');
print astr;
