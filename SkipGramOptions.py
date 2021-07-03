# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SkipGramOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SkipGramOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSkipGramOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SkipGramOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SkipGramOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SkipGramOptions
    def NgramSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SkipGramOptions
    def MaxSkipSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SkipGramOptions
    def IncludeAllNgrams(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(3)
def SkipGramOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNgramSize(builder, ngramSize): builder.PrependInt32Slot(0, ngramSize, 0)
def SkipGramOptionsAddNgramSize(builder, ngramSize):
    """This method is deprecated. Please switch to AddNgramSize."""
    return AddNgramSize(builder, ngramSize)
def AddMaxSkipSize(builder, maxSkipSize): builder.PrependInt32Slot(1, maxSkipSize, 0)
def SkipGramOptionsAddMaxSkipSize(builder, maxSkipSize):
    """This method is deprecated. Please switch to AddMaxSkipSize."""
    return AddMaxSkipSize(builder, maxSkipSize)
def AddIncludeAllNgrams(builder, includeAllNgrams): builder.PrependBoolSlot(2, includeAllNgrams, 0)
def SkipGramOptionsAddIncludeAllNgrams(builder, includeAllNgrams):
    """This method is deprecated. Please switch to AddIncludeAllNgrams."""
    return AddIncludeAllNgrams(builder, includeAllNgrams)
def End(builder): return builder.EndObject()
def SkipGramOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class SkipGramOptionsT(object):

    # SkipGramOptionsT
    def __init__(self):
        self.ngramSize = 0  # type: int
        self.maxSkipSize = 0  # type: int
        self.includeAllNgrams = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        skipGramOptions = SkipGramOptions()
        skipGramOptions.Init(buf, pos)
        return cls.InitFromObj(skipGramOptions)

    @classmethod
    def InitFromObj(cls, skipGramOptions):
        x = SkipGramOptionsT()
        x._UnPack(skipGramOptions)
        return x

    # SkipGramOptionsT
    def _UnPack(self, skipGramOptions):
        if skipGramOptions is None:
            return
        self.ngramSize = skipGramOptions.NgramSize()
        self.maxSkipSize = skipGramOptions.MaxSkipSize()
        self.includeAllNgrams = skipGramOptions.IncludeAllNgrams()

    # SkipGramOptionsT
    def Pack(self, builder):
        Start(builder)
        AddNgramSize(builder, self.ngramSize)
        AddMaxSkipSize(builder, self.maxSkipSize)
        AddIncludeAllNgrams(builder, self.includeAllNgrams)
        skipGramOptions = End(builder)
        return skipGramOptions
