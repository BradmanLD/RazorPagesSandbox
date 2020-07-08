# Sandbox
Sandbox for testing projects / new languages / etc

## RazorPages
Following the official Microsoft Docs for creating a basic razor pages web application.

## ASCII Image Converter
Small project to load an image and print it to the terminal in ASCII characters.

Based on: https://robertheaton.com/2018/12/08/programming-projects-for-advanced-beginners/

Known issues: Image sizing (better understanding how to use thumbnail to reduce the image size while still getting a viewable output).

Goals:
  - [x] Display test image properly
  - [ ] Add brightness calculation options
  - [ ] Add a way to invert the ASCII image for clarity
  - [ ] Add a method of automatically adding high color points back into the ASCII (i.e. anything above a certain RGB value is considered strong enough of a color to be stored)

## PDF Converter
Takes a file, reads it and creates a pdf with the content of the file.
TBD:
  - [x] Basic framework
  - [ ] Handle formatting (headings, font, font changes, etc)
  - [ ] Handle non-txt files as input
  - [ ] Get user input for the file path