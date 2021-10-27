from joshk.funcs import txt_to_json, to_properties, make_request, EXAMPLE_TEXT_IN


bibtex_json = txt_to_json(EXAMPLE_TEXT_IN)
properties = to_properties(bibtex_json)
make_request(properties)


properties['properties']['authors']