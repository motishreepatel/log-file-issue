# This file is reagarding examples on Classes and Objects
import logging
logging.basicConfig(filename = "test_st.log", filemode = 'w', level = logging.DEBUG)
#logging.basicConfig(filename='app.log', filemode='w'
# Exp-1
class iNeuron:
    try:
        about = "offers affordable online courses"
    except Exception as e:
        logging.exception("the exception that we will get is", str(e))

oneNeuron = iNeuron()
print(oneNeuron.about)
