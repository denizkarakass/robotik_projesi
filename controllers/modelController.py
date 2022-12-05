# IHA boyutlarını 2*2*2 şeklinde alıyorum.
# Engel, IHA, IKA konumları ROS aracılığıyla sensörlerden alınacak.
# ROS'dan MongoDB veritabanına aktarılıp güncel veriler buraya çekilebilir.

from ..models import iha1Model
from ..models import iha2Model
from ..models import iha3Model
from ..models import iha4Model
from ..models import iha5Model
from ..models import iha6Model

from ..models import ika1Model
from ..models import ika2Model


IKHAs = [iha1Model, iha2Model, iha3Model, iha4Model, iha5Model, iha6Model, ika1Model, ika2Model]

