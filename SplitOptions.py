# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SplitOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SplitOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSplitOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SplitOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SplitOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SplitOptions
    def NumSplits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def SplitOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNumSplits(builder, numSplits): builder.PrependInt32Slot(0, numSplits, 0)
def SplitOptionsAddNumSplits(builder, numSplits):
    """This method is deprecated. Please switch to AddNumSplits."""
    return AddNumSplits(builder, numSplits)
def End(builder): return builder.EndObject()
def SplitOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class SplitOptionsT(object):

    # SplitOptionsT
    def __init__(self):
        self.numSplits = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        splitOptions = SplitOptions()
        splitOptions.Init(buf, pos)
        return cls.InitFromObj(splitOptions)

    @classmethod
    def InitFromObj(cls, splitOptions):
        x = SplitOptionsT()
        x._UnPack(splitOptions)
        return x

    # SplitOptionsT
    def _UnPack(self, splitOptions):
        if splitOptions is None:
            return
        self.numSplits = splitOptions.NumSplits()

    # SplitOptionsT
    def Pack(self, builder):
        Start(builder)
        AddNumSplits(builder, self.numSplits)
        splitOptions = End(builder)
        return splitOptions