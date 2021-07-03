# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Uint8Vector(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Uint8Vector()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUint8Vector(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def Uint8VectorBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Uint8Vector
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Uint8Vector
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Uint8Vector
    def ValuesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Uint8Vector
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Uint8Vector
    def ValuesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Start(builder): builder.StartObject(1)
def Uint8VectorStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddValues(builder, values): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def Uint8VectorAddValues(builder, values):
    """This method is deprecated. Please switch to AddValues."""
    return AddValues(builder, values)
def StartValuesVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def Uint8VectorStartValuesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartValuesVector(builder, numElems)
def End(builder): return builder.EndObject()
def Uint8VectorEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
try:
    from typing import List
except:
    pass

class Uint8VectorT(object):

    # Uint8VectorT
    def __init__(self):
        self.values = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        uint8Vector = Uint8Vector()
        uint8Vector.Init(buf, pos)
        return cls.InitFromObj(uint8Vector)

    @classmethod
    def InitFromObj(cls, uint8Vector):
        x = Uint8VectorT()
        x._UnPack(uint8Vector)
        return x

    # Uint8VectorT
    def _UnPack(self, uint8Vector):
        if uint8Vector is None:
            return
        if not uint8Vector.ValuesIsNone():
            if np is None:
                self.values = []
                for i in range(uint8Vector.ValuesLength()):
                    self.values.append(uint8Vector.Values(i))
            else:
                self.values = uint8Vector.ValuesAsNumpy()

    # Uint8VectorT
    def Pack(self, builder):
        if self.values is not None:
            if np is not None and type(self.values) is np.ndarray:
                values = builder.CreateNumpyVector(self.values)
            else:
                StartValuesVector(builder, len(self.values))
                for i in reversed(range(len(self.values))):
                    builder.PrependUint8(self.values[i])
                values = builder.EndVector()
        Start(builder)
        if self.values is not None:
            AddValues(builder, values)
        uint8Vector = End(builder)
        return uint8Vector
