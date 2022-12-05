# IHA boyutlarını 2*2*2 şeklinde alıyorum.
# Engel, IHA, IKA konumları ROS aracılığıyla sensörlerden alınacak.
# ROS'dan MongoDB veritabanına aktarılıp güncel veriler buraya çekilebilir.

from ..models import iha1Model
from ..models import iha2Model
from ..models import iha3Model
from ..models import iha4Model
from ..models import iha5Model
from ..models import iha6Model
from ..models import iha7Model
from ..models import iha8Model

from ..models import ika1Model
from ..models import ika2Model

IHAs = [iha1Model, iha2Model, iha3Model, iha4Model, iha5Model, iha6Model, iha7Model, iha8Model]
IKAs = [ika1Model, ika2Model]
