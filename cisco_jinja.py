#!/usr/bin/env python3

import jinja2
import yaml

test_dict = {"vlan":3, "hostname":"Switch"}

template_directory = "./testfiles/templates/"
template_file = "test_template.config"
output_directory = ""
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_directory))
template = env.get_template(template_file)

print(template.render(test_dict))
