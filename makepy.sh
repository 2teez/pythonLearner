#!/usr/bin/env bash
# Description: Generate python script.
# Author: omitida
# Date: 04/04/25

function help() {
  script="${0}"
  echo "./script <options> <filename>"
  echo "Avaliable Options"
  echo "=================="
  echo "-d  to delete stated script"
  echo "-h  to display this help message"
  echo "-o  make a generic python script"
  echo "-r  to run the stated script"
  echo "-p  to make a python script"
  echo "-t  to make a python test script"
  echo "-T  to make a python testing task."
}

function make_py() {
  filename="${1}"
  extension="${filename##*.}"
  [[ -z "${extension}" ]] || [[ "${extension}" != ".py" ]] && filename="${filename}.py"
  echo "Creating ${filename}"
  echo "#!/usr/bin/env python3

def main() -> None:
    print(\"Start Here!\")

if __name__ == \"__main__\":
    main()
  " > "${filename}"
  # make the script executable
  chmod +x "${filename}"
}

[[ "${#}" -ne 2 ]] && help

optstring="d:r:p:o:t:T:h"
while getopts "${optstring}" opt; do
  case "$opt" in
   d)
     filename=$(basename "${OPTARG%.*}")
     file=$(find . -type f -iname "${filename,,}.*")
       [[ "${#file}" = 0 ]] && echo " No such file ${file}"  && break
       while read -r -p "Delete the file ${file} [y|n]: " ans; do
         case "${ans,,}" in
          y)
            echo "deleting... ${file}";
            rm -rf "${file}"
            echo "${file} deleted"
            break
            ;;
          n)
            echo "${file} NOT deleted!"
            break
            ;;
          *)
            echo "Invalid input. Can only use y for yes and n for no"
            continue
            ;;
          esac
       done
     ;;
   r)
     filename="${OPTARG}"
     python "${filename}"
     ;;
   o)
     filename="${OPTARG,,}"
     echo "Creating ${filename}"
     make_py "${filename}"
     python "${filename}"
     ;;
   p)
     filename="${OPTARG,,}"
     extension="${filename##*.}"
     echo "filename: ${filename}, extension: ${extension}"
     if [[ -z "${extension}" ]] || [[ "${extension}" != ".py" ]]; then
       filename="${filename}.py"
     fi

     # search to see if the file exist in the present folder
     my_pwd=$(dirname "${filename}")
     file=$(basename "$filename")
     number_file=$(find "${my_pwd}" -iname "${file}")
     if [[ -e "${number_file}" ]]; then
       while read -p "${file} exist. Do you want to overwrite? [y|n]: " -r ans; do
         case "${ans}" in
          y)
            echo "Start OVERWRITE!"
            break
            ;;
          n) exit 0
            ;;
          *) echo "Invalid Input. Only use y or n"
            continue
            ;;
         esac
         done
     fi
     echo "#!/usr/bin/env python3" > "${filename}"
     echo "" >> "${filename}"
     echo "" >> "${filename}"
     echo "def main() -> None:
     pass
     "  >> "${filename}"
     echo "if __name__ == '__main__':
     main()" >> "${filename}"
     # make the script executable
     chmod +x "${filename}"
     ;;
   t)
       # make a test file
       filename="${OPTARG}"
       filename="test_${filename}"
       make_py "${filename}"
       python "${filename}"
       ;;
    T)
       # creating a test task project
       filename="${OPTARG}"
       #
       # remove file extensions if one exists
       [ "${filename}" != "${filename%.*}" ] && filename="${filename%.*}"
       #
       # create the project directory
       if [ ! -d "${filename}" ]; then
           mkdir "${filename}"
       fi
       cd "${filename}" || exit
       # make a virtual environment
       virtual_env=".venv"
       python -m venv "${virtual_env}"
       #
       # activate the virtual environment
       source "${virtual_env}/bin/activate"
       # install dependencies
       pip install pytest pytest-watch
       # make directory for src, tests, and other project files
       mkdir -p src tests tests/func tests/unit
       # create init files for tests and src directories
       touch tests/func/__init__.py tests/unit/__init__.py src/__init__.py
       # create setup.py file
       echo "from setuptools import setup" >> setup.py
       echo "" >> setup.py
       echo "if __name__ == '__main__':" >> setup.py
       echo "    setup()" >> setup.py

       # create toml file
       # [build-system] section
       echo "[build-system]" >> "${filename}.toml"
       echo "requires = [\"setuptools >=68.0, wheel\"]" >> "${filename}.toml"
       echo "build-backend = \"setuptools.build_meta\"" >> "${filename}.toml"
       # [package] section
       echo "[package]" >> "${filename}.toml"
       echo "name = \"${filename}\"" >> "${filename}.toml"
       echo "version = \"0.1.0\"" >> "${filename}.toml"
       echo "description = \"\"" >> "${filename}.toml"
       echo "authors = []" >> "${filename}.toml"
       touch "${filename}.toml"

       ;;
   *) echo "Invalid options"
     exit 1
     ;;
   esac
done
