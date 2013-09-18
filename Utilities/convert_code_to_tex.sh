#! /bin/bash

# -----------------------------------------------------------------------------
#   Converts source-code files to LaTeX files with syntax highlighting
#
#   Version:    7
#   Date:       2013-09-18
#   Author:     René Schwaiger (sanssecours@f-m.fm)
#
# -----------------------------------------------------------------------------

# -- Constants ----------------------------------------------------------------

# To check for successful execution of a command
EXIT_SUCCESS="0"

# -- Functions ----------------------------------------------------------------

# -----------------------------------------------------------------------------
#   Checks the status of the last command and exits if there was an error.
#
#   Arguments:
#
#       $1 - The message which should be displayed if there was an error.
#
# -----------------------------------------------------------------------------
function exit_on_failure()
{
    if [ "$?" != "$EXIT_SUCCESS" ]; then
        echo "ERROR: ${1}" 1>&2
        exit 1
    fi
}

# -----------------------------------------------------------------------------
#   Convert source code files to (Xe)LaTeX files.
#
#   Converts all files in the folder `input_dir` to LaTeX code with syntax
#   highlighting. The resulting files will be stored, with the same base name
#   as the code files, only changing the extension to `.tex`, in the directory
#   `output_dir`.
#
#   Arguments:
#
#       $1 - The location of the source code files.
#       $2 - The directory where the converted LaTeX files will be saved.
#
# -----------------------------------------------------------------------------
function convert_to_tex()
{
    input_dir="$1"
    output_dir="$2"

    # Use highlight to convert the files
    # --------------------------------
    # -o Latex          Generate LaTeX output
    # -f                Omit header and footer in output
    # -t 4              Tabsize = 4
    # --no-trailing-nl  Omit trailing newline
    convert='highlight -O latex --encoding=utf8 --no-trailing-nl -f -t 4 -i'

    # Create output directory if it does not exist already
    mkdir -p "$output_dir"

    for code_file in "$input_dir"/*.*
        do
            tex_file="$output_dir"/"`basename ${code_file%\.*}`.tex"

            # Convert single file
            $convert "$code_file" > "$tex_file"
            # Check for error
            exit_on_failure "Could not convert "${code_file}""

            # Remove extra newline at the end of the generated code
            sed -n '1h;1!H;${;g;s/\\\\\n\\mbox/\\mbox/g;p;}' \
                "$tex_file" > tmp.txt
            mv tmp.txt "$tex_file"

            # Display conversion message on success
            echo "${code_file} => ${tex_file}"
    done
}

# -- Main ---------------------------------------------------------------------

input_dir=Pseudocode
output_dir=Code

# Convert the files
convert_to_tex "$input_dir" "$output_dir"

echo "Done with conversion"
