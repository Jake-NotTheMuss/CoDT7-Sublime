# This file is part of the T7-Sublime project.
# T7-Sublime is an enhanced syntax-highlighting package for (almost) all Call of Duty Black Ops III developer file formats.

import sublime, sublime_plugin

def insert_template(view, prepend, append = ''):
    cursor_pos = len(prepend)
    view.run_command('append', {'characters': prepend + append + '\n'})
    view.sel().clear()
    view.sel().add(sublime.Region(cursor_pos))

class NewCodt7LocalizedStringsCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/LocalizedStrings.sublime-syntax')

        prepend = \
        '// Note to translators:\n' \
        '// If a sentence is the same in your language then please change it to "#same"\n' \
        '//\n' \
        '// eg:\n' \
        '// LANG_ENGLISH  "HALT"\n' \
        '// LANG_GERMAN   "#same"\n' \
        '//\n' \
        '// (This is so we can tell which strings have been signed-off as ok to be the same words for QA\n' \
        '//  and because we do not store duplicate strings, which will then get exported again next time\n' \
        '//  as being untranslated.)\n' \
        '//\n' \
        'VERSION             "1"\n' \
        'CONFIG              "C:\\projects\\cod\\t7\\bin\\StringEd.cfg"\n' \
        'FILENOTES           ""\n\n'
        append  = '\n\nENDMARKER'

        insert_template(v, prepend, append)

        #v.run_command('new_string_definition')

class NewCodt7VisionCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/Vision.sublime-syntax')

        prepend = 'vkTT "'
        append  = '"\nvkTT ""\nvkTS ""\nvkTC ""\nvkTO ""\nvkRGB0 ""\nvkL0 ""\nvkM0 ""' \
                  '\nvkRGB1 ""\nvkL1 ""\nvkM1 ""\nvkRGB2 ""\nvkL2 ""\nvkRGB3 ""\nvkL3 ""' \
                  '\nvkM3 ""\nvkRGB4 ""\nvkL4 ""\nvkM4 ""\nvkRM ""'

        insert_template(v, prepend, append)

class NewCodt7SoundAliasCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/SoundAliasTable.sublime-syntax')

        template = 'Name,Behavior,Storage,FileSpec,FileSpecSustain,FileSpecRelease,Template,Loadspec,Secondary,' \
        'SustainAlias,ReleaseAlias,Bus,VolumeGroup,DuckGroup,Duck,ReverbSend,CenterSend,VolMin,VolMax,DistMin,' \
        'DistMaxDry,DistMaxWet,DryMinCurve,DryMaxCurve,WetMinCurve,WetMaxCurve,LimitCount,LimitType,' \
        'EntityLimitCount,EntityLimitType,PitchMin,PitchMax,PriorityMin,PriorityMax,PriorityThresholdMin,' \
        'PriorityThresholdMax,AmplitudePriority,PanType,Pan,Futz,Looping,RandomizeType,Probability,StartDelay,' \
        'EnvelopMin,EnvelopMax,EnvelopPercent,OcclusionLevel,IsBig,DistanceLpf,FluxType,FluxTime,Subtitle,Doppler,' \
        'ContextType,ContextValue,ContextType1,ContextValue1,ContextType2,ContextValue2,ContextType3,ContextValue3,' \
        'Timescale,IsMusic,IsCinematic,FadeIn,FadeOut,Pauseable,StopOnEntDeath,Compression,StopOnPlay,DopplerScale,' \
        'FutzPatch,VoiceLimit,IgnoreMaxDist,NeverPlayTwice,ContinuousPan,FileSource,FileSourceSustain,FileSourceRelease,' \
        'FileTarget,FileTargetSustain,FileTargetRelease,Platform,Language,OutputDevices,PlatformMask,WiiUMono,StopAlias,' \
        'DistanceLpfMin,DistanceLpfMax,FacialAnimationName,RestartContextLoops,SilentInCPZ,ContextFailsafe,GPAD,GPADOnly,' \
        'MuteVoice,MuteMusic,RowSourceFileName,RowSourceShortName,RowSourceLineNumber\n\n'

        insert_template(v, template)

        v.run_command('new_sound_alias_entry')


class NewCodt7SoundReverbCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/SoundReverbTable.sublime-syntax')

        template = 'Name,Loadspec,MasterReturn,EarlyInputLpf,EarlyFeedback,EarlySmear,EarlyBaseDelayMs,EarlyPreDelayMs,EarlyReturn,' \
        'NearInputLpf,NearFeedback,NearReturn,NearLowDamp,NearHighDamp,NearDecayTime,NearSmear,NearPreDelayMs,FarInputLpf,' \
        'FarFeedback,FarReturn,FarLowDamp,FarHighDamp,FarDecayTime,FarSmear,FarPreDelayMs\n\n'

        insert_template(v, template)

        v.run_command('new_sound_reverb_entry')

class NewCodt7SoundT5AliasCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/SoundT5AliasTable.sublime-syntax')

        template = 'name,file,template,loadspec,secondary,group,vol_min,vol_max,team_vol_mod,dist_min,dist_max,' \
        'dist_reverb_max,volume_falloff_curve,reverb_falloff_curve,volume_min_falloff_curve,reverb_min_falloff_curve,' \
        'limit_count,limit_type,entity_limit_count,entity_limit_type,pitch_min,pitch_max,team_pitch_mod,min_priority,' \
        'max_priority,min_priority_threshold,max_priority_threshold,spatialized,type,loop,randomize_type,probability,' \
        'start_delay,reverb_send,duck,pan,center_send,envelop_min,envelop_max,envelop_percentage,occlusion_level,' \
        'occlusion_wet_dry,is_big,distance_lpf,move_type,move_time,real_delay,subtitle,mature,doppler,futz,context_type,' \
        'context_value,compression,timescale,music,fade_in,fade_out,pc_format,pause,stop_on_death,bus,snapshot,voice_limit,' \
        'file_xenon,file_size_xenon,file_ps3,file_size_ps3,file_pc,file_size_pc,file_wii,file_size_wii,source_csv,language\n\n'

        insert_template(v, template)

        v.run_command('new_sound_t5_alias_entry')

class NewCodt7SoundT5ReverbCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/SoundT5ReverbTable.sublime-syntax')

        template = 'name,room,roomHF,roomRolloffFactor,decayTime,decayHFRatio,reflections,reflectionsDelay,' \
        'reverb,reverbDelay,diffusion,density,HFReference\n\n'

        insert_template(v, template)

        v.run_command('new_sound_t5_reverb_entry')

class NewCodt7SoundAmbientCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()

        v.assign_syntax('Packages/CoDT7 Formats/SoundAmbientTable.sublime-syntax')

        template = 'Name,Loadspec,DefaultRoom,Reverb,NearVerb,FarVerb,ReverbDryLevel,ReverbWetLevel,' \
        'EntityContextType0,EntityContextValue0,EntityContextType1,EntityContextValue1,EntityContextType2,' \
        'EntityContextValue2,GlobalContextType,GlobalContextValue,Loop,Duck\n\n'

        insert_template(v, template)

        v.run_command('new_sound_ambient_entry')
