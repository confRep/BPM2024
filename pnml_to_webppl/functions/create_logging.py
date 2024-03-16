def log_transitions(function_str, variable_dict):
    # Start of the JS function template
    function_str += """var log_transition = function(transition) {\nif (globalStore.printTransitions) {\nprint(transition + " ["""

    # Dynamically append each variable part, correctly handling quotation marks
    variable_parts = [f"{key} = " + '"+ globalStore.' + f"{key}" + ' + "' for key in variable_dict]
    function_str += ', '.join(variable_parts)

    # Close the print statement and function
    function_str += "]\");\n}\n}\n\n"

    return function_str


def log_state(function_str, dpn, variable_dict):
    # Start of the JS function template
    function_str += """var log_state = function() {\nif (globalStore.logState) {\n"""
    places_list = list(dpn.net.places)

    m_part = "print(\"M["
    places_parts = [f"" + '"+ globalStore.' + f"{place}" + ' + "' for place in places_list]
    m_part += ', '.join(places_parts)
    m_part += "]\""
    function_str += m_part

    # Dynamically append each variable part, correctly handling quotation marks
    variable_parts = [f"{key} = " + '"+ globalStore.' + f"{key}" + ' + "' for key in variable_dict]
    function_str += " + \" V[" + ', '.join(variable_parts)
    function_str += "]\""

    function_str += ");\n}\n}\n\n"

    return function_str


def create_logging(function_str, dpn, verbose):
    if verbose:
        function_str = log_transitions(function_str, dpn.variable_information)
        function_str = log_state(function_str, dpn, dpn.variable_information)

    return function_str
