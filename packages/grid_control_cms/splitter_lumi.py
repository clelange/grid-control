# | Copyright 2007-2016 Karlsruhe Institute of Technology
# |
# | Licensed under the Apache License, Version 2.0 (the "License");
# | you may not use this file except in compliance with the License.
# | You may obtain a copy of the License at
# |
# |     http://www.apache.org/licenses/LICENSE-2.0
# |
# | Unless required by applicable law or agreed to in writing, software
# | distributed under the License is distributed on an "AS IS" BASIS,
# | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# | See the License for the specific language governing permissions and
# | limitations under the License.

from grid_control.datasets import DataProvider, DataSplitter
from python_compat import lmap

class RunSplitter(DataSplitter.getClass('MetadataSplitter')):
	def metaKey(self, metadataNames, block, fi):
		selRunRange = self.setup(self._config.getInt, block, 'run range', 1)
		mdIdx = metadataNames.index('Runs')
		return lmap(lambda r: int(r / selRunRange), fi[DataProvider.Metadata][mdIdx])