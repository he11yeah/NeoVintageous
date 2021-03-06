
# well-known variables
_SPECIAL_STRINGS = {
    '<leader>': 'mapleader',
    '<localleader>': 'maplocalleader',
}


_DEFAULTS = {
    'mapleader': '\\',
    'maplocalleader': '\\'
}


_VARIABLES = {
}


def expand_keys(seq):
    """Replace well-known variables in key names with their corresponding values."""
    leader = var_name = None

    # TODO(guillermooo): Can these variables appear in the middle of a
    # sequence instead of at the beginning only?
    if seq.lower().startswith('<leader>'):
        var_name = '<leader>'
        leader = _VARIABLES.get('mapleader', _DEFAULTS.get('mapleader'))

    if seq.lower().startswith('<localleader>'):
        var = '<localleader>'
        local_leader = _VARIABLES.get('maplocalleader', _DEFAULTS.get('maplocalleader'))

    try:
        return leader + seq[len(var_name):]
    except TypeError:
        return seq


def is_key_name(name):
    return name.lower() in _SPECIAL_STRINGS


def get(name):
    name = name.lower()
    name = _SPECIAL_STRINGS.get(name, name)

    return _VARIABLES.get(name, _DEFAULTS.get(name))


def set_(name, value):
    # TODO(guillermooo): Set vars in settings.
    _VARIABLES[name] = value


class Variables(object):
    """
    Store variables during the current Sublime Text session.

    Meant to be used as a descriptor with `State`.
    """

    def __get__(self, instance, owner):
        self.view = instance.view
        self.settings = instance.settings

        return self

    def get(self, name):
        return get(name)

    def set(self, name, value):
        return set_(name, value)
