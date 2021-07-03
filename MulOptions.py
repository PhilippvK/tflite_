# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MulOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MulOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMulOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def MulOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # MulOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MulOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def MulOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def MulOptionsAddFusedActivationFunction(builder, fusedActivationFunction):
    """This method is deprecated. Please switch to AddFusedActivationFunction."""
    return AddFusedActivationFunction(builder, fusedActivationFunction)
def End(builder): return builder.EndObject()
def MulOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)

class MulOptionsT(object):

    # MulOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        mulOptions = MulOptions()
        mulOptions.Init(buf, pos)
        return cls.InitFromObj(mulOptions)

    @classmethod
    def InitFromObj(cls, mulOptions):
        x = MulOptionsT()
        x._UnPack(mulOptions)
        return x

    # MulOptionsT
    def _UnPack(self, mulOptions):
        if mulOptions is None:
            return
        self.fusedActivationFunction = mulOptions.FusedActivationFunction()

    # MulOptionsT
    def Pack(self, builder):
        Start(builder)
        AddFusedActivationFunction(builder, self.fusedActivationFunction)
        mulOptions = End(builder)
        return mulOptions