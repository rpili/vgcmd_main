from psychopy.misc import fromFile

datFile = fromFile('1_tg_main_2019_Nov_05_0211.psydat')
#get info (added when the handler was created)
# datFile has experiment handler information
print(dir(datFile))
# for trialHandler data
trialHandler = datFile
# see list of trialHandler parameters
trialHandlerParams = dir(datFile)
print(trialHandlerParams)
print(trialHandler.extraInfo)


"""
# View data
print(trialHandler.data)
print(trialHandler.data['ran'])
print(trialHandler.data['order'])
print(trialHandler.data['key_resp_2.rt'])
"""