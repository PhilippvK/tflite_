# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LessEqualOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LessEqualOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsLessEqualOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def LessEqualOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LessEqualOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def Start(builder): builder.StartObject(0)
def LessEqualOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def End(builder): return builder.EndObject()
def LessEqualOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class LessEqualOptionsT(object):

    # LessEqualOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        lessEqualOptions = LessEqualOptions()
        lessEqualOptions.Init(buf, pos)
        return cls.InitFromObj(lessEqualOptions)

    @classmethod
    def InitFromObj(cls, lessEqualOptions):
        x = LessEqualOptionsT()
        x._UnPack(lessEqualOptions)
        return x

    # LessEqualOptionsT
    def _UnPack(self, lessEqualOptions):
        if lessEqualOptions is None:
            return

    # LessEqualOptionsT
    def Pack(self, builder):
        Start(builder)
        lessEqualOptions = End(builder)
        return lessEqualOptions
