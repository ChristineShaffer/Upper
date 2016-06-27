"""
    Add Anchors - Adds <a href="#">List Item</a> to each item in a list
    pasted to input screen.
    Copyright (C) 2016 Christine Shaffer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


"""
Program gets uppercase each element in inputted list then outputs on screen
"""


def format_list(a_list):
    for line in a_list:
        print(line.upper())


def main():

    while True:
        a_list = []
        end = ''    # Ends when this string is seen
        print("Paste list here and hit enter twice:")
        for line in iter(input, end):
            a_list.append(line)

        if a_list:
            break
        else:
            print("Please enter any value")

    # Format list and output
    format_list(a_list)


if __name__ == "__main__":
    main()
