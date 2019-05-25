`# Cython - optimising static compiler
An easy way to create compiled libraries out of Python modules.

#### The Following commands to install Cython in python (if you have python installed).
   `pip install cython`
   
#### Add the following python script to your project folder as compile.py
   `from distutils.core import setup`<br>
   `from distutils.extension import Extension`<br>
   `from Cython.Distutils import build_ext`<br>
   `ext_modules = [`<br>
       `Extension("mymodule1",  ["mymodule1.py"]),`<br>
       `Extension("mymodule2",  ["mymodule2.py"]),`<br>
       `# add all your modules that need be compiled ...`<br>
   `]`<br>
   `setup(`<br>
       `name = 'My Program Name',`<br>
       `cmdclass = {'build_ext': build_ext},`<br>
       `ext_modules = ext_modules`<br>
   `)`

  

#### There should be an entry point or main file in your project. Assume you have one main.py entry point file. 
  if __name__ == "__main__":
    main()
    

#### Run Compile.py script.
   `python compile.py build_ext --inplace`

   
#### The above command should generate .c and .pyd files if you are working on Windows Machine.
   `main.c`
   `main.cp36-win_amd64.pyd`


#### Now you can delete .py and .c files. You can use .pyd file just by importing it in python.
   import main

#### Thanks :)
