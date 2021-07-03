# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FillOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FillOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFillOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def FillOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # FillOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def Start(builder): builder.StartObject(0)
def FillOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def End(builder): return builder.EndObject()
def FillOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class FillOptionsT(object):

    # FillOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        fillOptions = FillOptions()
        fillOptions.Init(buf, pos)
        return cls.InitFromObj(fillOptions)

    @classmethod
    def InitFromObj(cls, fillOptions):
        x = FillOptionsT()
        x._UnPack(fillOptions)
        return x

    # FillOptionsT
    def _UnPack(self, fillOptions):
        if fillOptions is None:
            return

    # FillOptionsT
    def Pack(self, builder):
        Start(builder)
        fillOptions = End(builder)
        return fillOptions