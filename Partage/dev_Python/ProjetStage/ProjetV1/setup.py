from cx_Freeze import setup, Executable

setup(
	name = "Phenotypage",
	version = "1",
	description = "Faire des photos",
	executables = [Executable("VueV2.py")],
)
