
# This is a helper module for table_column_order.py
# It helps with matching the casing convention in
# the field names of a loaded table

CASE_FLAT = 0
CASE_SNAKE = 1
CASE_CAMEL = 2
CASE_CAMEL_UPPER = 3
CASE_CAPITALIZED = 4
CASE_UNKNOWN = -1
CASE_DEFAULT = CASE_CAMEL_UPPER

def get_casing_type(field_names):
    if field_names is None:
        return CASE_UNKNOWN

    i = 0
    n_fields = len(field_names)
    field_name = None
    while i < n_fields and (field_name is None or not field_name.strip()):
        field_name = field_names[i]
        i += 1
    # invalid input
    if field_name is None or not field_name.strip():
        return CASE_UNKNOWN

    # first char is upper
    if field_name[0].isupper():
        # every other char is lower
        if field_name.capitalize() == field_name:
            return CASE_CAPITALIZED
        # upper camel cased
        else:
            return CASE_CAMEL_UPPER
    # first char is not upper
    else:
        # all chars are lower
        if field_name.lower() == field_name:
            return CASE_FLAT
        # camel cased
        else:
            return CASE_CAMEL

sound_alias_fields = [ 'Name', 'Behavior', 'Storage', 'FileSpec', 'FileSpecSustain', 'FileSpecRelease', 'Template', 'Loadspec', 'Secondary', 'SustainAlias', 'ReleaseAlias', 'Bus', 'VolumeGroup', 'DuckGroup', 'Duck', 'ReverbSend', 'CenterSend', 'VolMin', 'VolMax', 'DistMin', 'DistMaxDry', 'DistMaxWet', 'DryMinCurve', 'DryMaxCurve', 'WetMinCurve', 'WetMaxCurve', 'LimitCount', 'LimitType', 'EntityLimitCount', 'EntityLimitType', 'PitchMin', 'PitchMax', 'PriorityMin', 'PriorityMax', 'PriorityThresholdMin', 'PriorityThresholdMax', 'AmplitudePriority', 'PanType', 'Pan', 'Futz', 'Looping', 'RandomizeType', 'Probability', 'StartDelay', 'EnvelopMin', 'EnvelopMax', 'EnvelopPercent', 'OcclusionLevel', 'IsBig', 'DistanceLpf', 'FluxType', 'FluxTime', 'Subtitle', 'Doppler', 'ContextType', 'ContextValue', 'ContextType1', 'ContextValue1', 'ContextType2', 'ContextValue2', 'ContextType3', 'ContextValue3', 'Timescale', 'IsMusic', 'IsCinematic', 'FadeIn', 'FadeOut', 'Pauseable', 'StopOnEntDeath', 'Compression', 'StopOnPlay', 'DopplerScale', 'FutzPatch', 'VoiceLimit', 'IgnoreMaxDist', 'NeverPlayTwice', 'ContinuousPan', 'FileSource', 'FileSourceSustain', 'FileSourceRelease', 'FileTarget', 'FileTargetSustain', 'FileTargetRelease', 'Platform', 'Language', 'OutputDevices', 'PlatformMask', 'WiiUMono', 'StopAlias', 'DistanceLpfMin', 'DistanceLpfMax', 'FacialAnimationName', 'RestartContextLoops', 'SilentInCPZ', 'ContextFailsafe', 'GPAD', 'GPADOnly', 'MuteVoice', 'MuteMusic', 'RowSourceFileName', 'RowSourceShortName', 'RowSourceLineNumber' ]
sound_reverb_fields =  [ 'Name', 'Loadspec', 'MasterReturn', 'EarlyInputLpf', 'EarlyFeedback', 'EarlySmear', 'EarlyBaseDelayMs', 'EarlyPreDelayMs', 'EarlyReturn', 'NearInputLpf', 'NearFeedback', 'NearReturn', 'NearLowDamp', 'NearHighDamp', 'NearDecayTime', 'NearSmear', 'NearPreDelayMs', 'FarInputLpf', 'FarFeedback', 'FarReturn', 'FarLowDamp', 'FarHighDamp', 'FarDecayTime', 'FarSmear', 'FarPreDelayMs' ]
sound_ambient_fields = [ 'Name', 'Loadspec', 'DefaultRoom', 'Reverb', 'NearVerb', 'FarVerb', 'ReverbDryLevel', 'ReverbWetLevel', 'EntityContextType0', 'EntityContextValue0', 'EntityContextType1', 'EntityContextValue1', 'EntityContextType2', 'EntityContextValue2', 'GlobalContextType', 'GlobalContextValue', 'Loop', 'Duck' ]

table_field_names = {
    'text.codt7.table.sound.alias': sound_alias_fields,
    'text.codt7.table.sound.reverb': sound_reverb_fields,
    'text.codt7.table.sound.ambient': sound_ambient_fields
}

table_field_name_list = None

def cased_field_names_supported():
    return table_field_name_list is not None

def set_field_name_list_for_scope(scope):
    global table_field_name_list
    table_field_name_list = table_field_names.get(scope)

def get_field_name_with_casing_type(index, casing_type):
    if casing_type == CASE_UNKNOWN:
        casing_type = CASE_DEFAULT

    if table_field_name_list is None or index >= len(table_field_name_list):
        return ''

    field_name = table_field_name_list[index]

    if casing_type == CASE_CAPITALIZED:
        return field_name.capitalize()
    elif casing_type == CASE_CAMEL:
        return field_name[0].lower() + field_name[1:]
    elif casing_type == CASE_FLAT:
        return field_name.lower()

    return field_name
