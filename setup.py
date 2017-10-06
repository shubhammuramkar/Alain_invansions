from cx_Freeze import setup , Executable

setup(name = "Alain Invansion",
	version = '1.0',
	description = 'Game for Fun',
	executables = [Executable("alien_invasion.py")]) 


# import cx_Freeze

# executables = [cx_Freeze.Executable("alien_invasion.py")]

# cx_Freeze.setup(
#     name="A bit Racey",
#     options={
#     "build_exe": { "packages":["pygame"] }
#     },
#     executables = executables

#     )