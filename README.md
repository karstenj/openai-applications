# OpenAI Examples
A collection of [OpenAI](https://openai.com/) examples using the Python API.

## Quickstart
### Required Packages
* [aocd](https://github.com/wimglenn/advent-of-code-data)
    * `pip install aocd`
* [openai](https://github.com/openai/openai-python)
    * `pip install openai`
### Environment Variables
* AOC_SESSION - Session ID taken from browser cookie information
* OPENAI_API_KEY - Create an API key in your OpenAI account and enter it's value in this variable

## Examples
### Advent of Code
Use ostwilkens AoC solution https://github.com/ostwilkens/aoc2022.

Generated solutions for Advent of Code 2022:
* [day1/part1](aoc/2022-1-1.py)
* [day1/part2](aoc/2022-1-2.py)
* [day3/part1](aoc/2022-3-1.py)
* [day3/part2](aoc/2022-3-2.py)
* [day3/part1](aoc/2022-4-1.py)
* [day3/part2](aoc/2022-4-2.py)

### Cyberdojo
In this example an algorithmic problem description taken from [cyber-dojo.org](https://cyber-dojo.org) is passed to the OpenAI model text-davinci-003. 
The following files have to be created per algorithmic problem:
* `<problem name>_desc.txt` - problem description
* `<problem name>_func.txt` - function prototype
* `<problem name>_input_<ident>.txt` - input data for testing

### UML Diagram

### HTML Page

## Special thanks to
* The OpenAI team
* Eric Wastl for creating https://adventofcode.com/
* wimglenn and contributors of https://github.com/wimglenn/advent-of-code-data
* ostwilkens sharing his OpenAI AoC solution https://github.com/ostwilkens/aoc2022 
