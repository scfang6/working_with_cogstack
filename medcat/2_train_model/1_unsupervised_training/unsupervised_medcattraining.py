from medcat.cat import CAT
import logging
import sys
sys.path.append('../../../')
from cogstack import CogStack
from credentials import *

medcat_logger = logging.getLogger('medcat')
fh = logging.FileHandler('medcat.log')
medcat_logger.addHandler(fh)

###Change parameters here###
cogstack_indices = []  # list of cogstack indexes here
text_columns = ['body_analysed']  # list of all text containing fields
model_pack_path = '../../../data/medcat_models/modelpack/'
model_pack_name = ''
output_modelpack_name = ''  # name of modelpack to save

cs = CogStack(hosts, api_username=api_username, api_password=api_password, api=True)
df = cs.DataFrame(index=cogstack_indices, columns=text_columns)

cat = CAT.load_model_pack(model_pack_path+model_pack_name)
cat.cdb.print_stats()
cat.train(data_iterator=df[text_columns].iterrows(),
          nepochs=1,
          fine_tune=True,
          progress_print=10000,
          is_resumed=False)

cat.cdb.print_stats()

cat.create_model_pack(save_dir_path=model_pack_path, model_pack_name=output_modelpack_name)
