# Image Prompt Generator

## Overview
Image Prompt Generator is a Python script that generates prompts for image generation based on customizable templates. It allows users to define templates with placeholders for various elements such as adjectives, nouns, colors, artistic styles, and specific style elements. The script randomly selects words from predefined lists to fill in the placeholders and create diverse and imaginative prompts for generating images.

## Features
- Customizable prompt templates
- Support for a wide range of placeholders and word candidates
- Simple and easy-to-use interface
- Allows for the generation of diverse image prompts for artistic and creative projects

## Usage
1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the `image_prompt_generator.py` script with Python.
4. Follow the instructions to input the path to your external JSON file containing prompt templates.
5. The script will generate a random prompt based on the provided template and display it in the console.

## Example Prompt Template JSON
```json
{
  "template": "Create an abstract artwork that explores the concept of <concept>. The color palette should include <color1>, <color2>, and <color3>. Use an <artistic_style> style with a focus on <specific_style_element> for a visually striking piece.",
  "candidates": {
    "<concept>": ["emotion", "chaos", "harmony", "transformation", "infinity", "movement", "energy", "balance", "contrast", "serenity"],
    "<color1>": ["red", "blue", "yellow", "green", "purple", "orange", "turquoise", "pink", "lime", "indigo"],
    "<color2>": ["orange", "turquoise", "pink", "lime", "indigo", "gold", "silver", "bronze", "copper", "platinum"],
    "<color3>": ["gold", "silver", "bronze", "copper", "platinum", "crimson", "emerald", "azure", "violet", "amber"],
    "<artistic_style>": ["abstract expressionism", "minimalism", "geometric abstraction", "post-painterly abstraction", "lyrical abstraction", "cubism", "fauvism", "suprematism", "surrealism", "op art"],
    "<specific_style_element>": ["texture", "form", "composition", "contrast", "energy", "line", "shape", "space", "pattern", "abstraction"]
  }
}
