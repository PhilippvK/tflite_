# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ReverseV2Options(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ReverseV2Options()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsReverseV2Options(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ReverseV2OptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ReverseV2Options
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def Start(builder): builder.StartObject(0)
def ReverseV2OptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def End(builder): return builder.EndObject()
def ReverseV2OptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class ReverseV2OptionsT(object):

    # ReverseV2OptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        reverseV2Options = ReverseV2Options()
        reverseV2Options.Init(buf, pos)
        return cls.InitFromObj(reverseV2Options)

    @classmethod
    def InitFromObj(cls, reverseV2Options):
        x = ReverseV2OptionsT()
        x._UnPack(reverseV2Options)
        return x

    # ReverseV2OptionsT
    def _UnPack(self, reverseV2Options):
        if reverseV2Options is None:
            return

    # ReverseV2OptionsT
    def Pack(self, builder):
        Start(builder)
        reverseV2Options = End(builder)
        return reverseV2Options