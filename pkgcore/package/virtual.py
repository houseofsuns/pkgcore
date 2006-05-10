# Copyright: 2005 Jason Stubbs <jstubbs@gentoo.org>
# License: GPL2

from pkgcore.package import metadata
from pkgcore.restrictions.packages import OrRestriction

class package(metadata.package):

	def __getattr__ (self, key):
		val = None
		if key == "rdepends":
			val = self.data
		elif key == "depends":
			val = OrRestriction()
		elif key == "provides":
			val = OrRestriction()
		elif key == "metapkg":
			val = True
		elif key == "slot":
			val = "0"
		else:
			return super(package, self).__getattr__(key)
		self.__dict__[key] = val
		return val

	def _fetch_metadata(self):
		data = self._parent._parent_repo._fetch_metadata(self)
		return data


class factory(metadata.factory):
	child_class = package

	def __init__(self, parent, *args, **kwargs):
		super(factory, self).__init__(parent, *args, **kwargs)
