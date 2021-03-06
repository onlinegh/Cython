# Cython - optimising static compiler.
An easy way to create compiled libraries out of Python modules.

#### The Following commands to install Cython in python (if you have python installed).
   `pip install cython`
   
#### Add the following python script to your project folder as compile.py. Please add your python modules that you need to be compiled in Extension().
   ```python
   from distutils.core import setup
   from distutils.extension import Extension
   from Cython.Distutils import build_ext
   ext_modules = [
       Extension("module1",  ["module1.py"]),
       Extension("module2",  ["module2.py"]),
       #all your modules that need be compiled ...
   ]
   setup(
      name = 'My Program Name',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules
   )
   ```
  

#### There should be an entry point or main file in your project. Assume you have one main.py entry point file. 
  ```
  if __name__ == "__main__":
    main()
  ```  

#### Run Compile.py script.
   `python compile.py build_ext --inplace`

   
#### The above command should generate .c and .pyd files if you are working on Windows Machine.
   `main.c`<br>
   `main.cp36-win_amd64.pyd`


#### Now you can delete .py and .c files. You can use .pyd file just by importing it in python.
   `import main`

#### Thanks :)
