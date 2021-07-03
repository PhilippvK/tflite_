# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BidirectionalSequenceLSTMOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BidirectionalSequenceLSTMOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBidirectionalSequenceLSTMOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BidirectionalSequenceLSTMOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # BidirectionalSequenceLSTMOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BidirectionalSequenceLSTMOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # BidirectionalSequenceLSTMOptions
    def CellClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # BidirectionalSequenceLSTMOptions
    def ProjClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # BidirectionalSequenceLSTMOptions
    def MergeOutputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BidirectionalSequenceLSTMOptions
    def TimeMajor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # BidirectionalSequenceLSTMOptions
    def AsymmetricQuantizeInputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(6)
def BidirectionalSequenceLSTMOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def BidirectionalSequenceLSTMOptionsAddFusedActivationFunction(builder, fusedActivationFunction):
    """This method is deprecated. Please switch to AddFusedActivationFunction."""
    return AddFusedActivationFunction(builder, fusedActivationFunction)
def AddCellClip(builder, cellClip): builder.PrependFloat32Slot(1, cellClip, 0.0)
def BidirectionalSequenceLSTMOptionsAddCellClip(builder, cellClip):
    """This method is deprecated. Please switch to AddCellClip."""
    return AddCellClip(builder, cellClip)
def AddProjClip(builder, projClip): builder.PrependFloat32Slot(2, projClip, 0.0)
def BidirectionalSequenceLSTMOptionsAddProjClip(builder, projClip):
    """This method is deprecated. Please switch to AddProjClip."""
    return AddProjClip(builder, projClip)
def AddMergeOutputs(builder, mergeOutputs): builder.PrependBoolSlot(3, mergeOutputs, 0)
def BidirectionalSequenceLSTMOptionsAddMergeOutputs(builder, mergeOutputs):
    """This method is deprecated. Please switch to AddMergeOutputs."""
    return AddMergeOutputs(builder, mergeOutputs)
def AddTimeMajor(builder, timeMajor): builder.PrependBoolSlot(4, timeMajor, 1)
def BidirectionalSequenceLSTMOptionsAddTimeMajor(builder, timeMajor):
    """This method is deprecated. Please switch to AddTimeMajor."""
    return AddTimeMajor(builder, timeMajor)
def AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs): builder.PrependBoolSlot(5, asymmetricQuantizeInputs, 0)
def BidirectionalSequenceLSTMOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    """This method is deprecated. Please switch to AddAsymmetricQuantizeInputs."""
    return AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs)
def End(builder): return builder.EndObject()
def BidirectionalSequenceLSTMOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class BidirectionalSequenceLSTMOptionsT(object):

    # BidirectionalSequenceLSTMOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int
        self.cellClip = 0.0  # type: float
        self.projClip = 0.0  # type: float
        self.mergeOutputs = False  # type: bool
        self.timeMajor = True  # type: bool
        self.asymmetricQuantizeInputs = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        bidirectionalSequenceLSTMOptions = BidirectionalSequenceLSTMOptions()
        bidirectionalSequenceLSTMOptions.Init(buf, pos)
        return cls.InitFromObj(bidirectionalSequenceLSTMOptions)

    @classmethod
    def InitFromObj(cls, bidirectionalSequenceLSTMOptions):
        x = BidirectionalSequenceLSTMOptionsT()
        x._UnPack(bidirectionalSequenceLSTMOptions)
        return x

    # BidirectionalSequenceLSTMOptionsT
    def _UnPack(self, bidirectionalSequenceLSTMOptions):
        if bidirectionalSequenceLSTMOptions is None:
            return
        self.fusedActivationFunction = bidirectionalSequenceLSTMOptions.FusedActivationFunction()
        self.cellClip = bidirectionalSequenceLSTMOptions.CellClip()
        self.projClip = bidirectionalSequenceLSTMOptions.ProjClip()
        self.mergeOutputs = bidirectionalSequenceLSTMOptions.MergeOutputs()
        self.timeMajor = bidirectionalSequenceLSTMOptions.TimeMajor()
        self.asymmetricQuantizeInputs = bidirectionalSequenceLSTMOptions.AsymmetricQuantizeInputs()

    # BidirectionalSequenceLSTMOptionsT
    def Pack(self, builder):
        Start(builder)
        AddFusedActivationFunction(builder, self.fusedActivationFunction)
        AddCellClip(builder, self.cellClip)
        AddProjClip(builder, self.projClip)
        AddMergeOutputs(builder, self.mergeOutputs)
        AddTimeMajor(builder, self.timeMajor)
        AddAsymmetricQuantizeInputs(builder, self.asymmetricQuantizeInputs)
        bidirectionalSequenceLSTMOptions = End(builder)
        return bidirectionalSequenceLSTMOptions
