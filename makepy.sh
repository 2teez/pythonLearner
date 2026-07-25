#!/usr/bin/env bash
# Description: Generate python script.
# Author: omitida
# Date: 04/04/25

function help() {
  script="${0}"
  echo "./script <options> <filename>"
  echo "Options Uses:"
  echo "-d  to delete stated script"
  echo "-r  to run the stated script"
  echo "-p  to make a python script"
}

[[ "${#}" -ne 2 ]] && help

optstring="d:r:p:h"
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
   p)
     filename="${OPTARG,,}"
     extension="${filename##*.}"
     [[ -z "${extension}" ]] || [[ "${extension}" != ".py" ]] && filename="${filename}.py"

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
   *) echo "Invalid options"
     exit 1
     ;;
   esac
done
