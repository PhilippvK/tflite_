# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SplitVOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SplitVOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSplitVOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SplitVOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SplitVOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SplitVOptions
    def NumSplits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def SplitVOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNumSplits(builder, numSplits): builder.PrependInt32Slot(0, numSplits, 0)
def SplitVOptionsAddNumSplits(builder, numSplits):
    """This method is deprecated. Please switch to AddNumSplits."""
    return AddNumSplits(builder, numSplits)
def End(builder): return builder.EndObject()
def SplitVOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class SplitVOptionsT(object):

    # SplitVOptionsT
    def __init__(self):
        self.numSplits = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        splitVOptions = SplitVOptions()
        splitVOptions.Init(buf, pos)
        return cls.InitFromObj(splitVOptions)

    @classmethod
    def InitFromObj(cls, splitVOptions):
        x = SplitVOptionsT()
        x._UnPack(splitVOptions)
        return x

    # SplitVOptionsT
    def _UnPack(self, splitVOptions):
        if splitVOptions is None:
            return
        self.numSplits = splitVOptions.NumSplits()

    # SplitVOptionsT
    def Pack(self, builder):
        Start(builder)
        AddNumSplits(builder, self.numSplits)
        splitVOptions = End(builder)
        return splitVOptions
