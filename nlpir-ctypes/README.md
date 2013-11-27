nlpir-ctypes
============

### Idea
This approach is inspired by this link [Python下调用NLPIR(ICTCLAS2013)的ctype做法](http://ictclas.nlpir.org/newsDetail?DocId=382) which demonstrates the Win32 platform.

### How to hack
I made it run for Linux32 platform and as versions go by, the function symbols may need to be changed with newer `libNLPIR.so/NLPIR.dll`.

You may hack follow this:

*   replace `nlpir = CDLL(the_library_path)` in `nlpir-ctypes.py`
*   using a right tool to dump the exported NLPIR function symbols(For Linux, `nm` or `objdump` maybe. And Windows you may try `dumpbin` or [DLL Exp](http://www.nirsoft.net/utils/dll_export_viewer.html))
*   update the function symbols within the `getattr` invoke
*   check the function parameters to make `fillprototype` right if necessary
*   you are done:-)

### What's next
As you can see, it should not be difficult to add linux64 and win64 support:-)

**Note**

Please use the right python interpreter, for `*.so` under Linux and for `*.dll` under Windows, or `CDLL` will fail.
