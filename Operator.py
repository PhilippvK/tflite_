# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Operator(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Operator()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOperator(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def OperatorBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Operator
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Operator
    def OpcodeIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Operator
    def Inputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Operator
    def InputsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Operator
    def InputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Operator
    def InputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Operator
    def Outputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Operator
    def OutputsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Operator
    def OutputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Operator
    def OutputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Operator
    def BuiltinOptionsType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Operator
    def BuiltinOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Operator
    def CustomOptions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Operator
    def CustomOptionsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Operator
    def CustomOptionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Operator
    def CustomOptionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Operator
    def CustomOptionsFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Operator
    def MutatingVariableInputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.BoolFlags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Operator
    def MutatingVariableInputsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.BoolFlags, o)
        return 0

    # Operator
    def MutatingVariableInputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Operator
    def MutatingVariableInputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # Operator
    def Intermediates(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Operator
    def IntermediatesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Operator
    def IntermediatesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Operator
    def IntermediatesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

def Start(builder): builder.StartObject(9)
def OperatorStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddOpcodeIndex(builder, opcodeIndex): builder.PrependUint32Slot(0, opcodeIndex, 0)
def OperatorAddOpcodeIndex(builder, opcodeIndex):
    """This method is deprecated. Please switch to AddOpcodeIndex."""
    return AddOpcodeIndex(builder, opcodeIndex)
def AddInputs(builder, inputs): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(inputs), 0)
def OperatorAddInputs(builder, inputs):
    """This method is deprecated. Please switch to AddInputs."""
    return AddInputs(builder, inputs)
def StartInputsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def OperatorStartInputsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartInputsVector(builder, numElems)
def AddOutputs(builder, outputs): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(outputs), 0)
def OperatorAddOutputs(builder, outputs):
    """This method is deprecated. Please switch to AddOutputs."""
    return AddOutputs(builder, outputs)
def StartOutputsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def OperatorStartOutputsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOutputsVector(builder, numElems)
def AddBuiltinOptionsType(builder, builtinOptionsType): builder.PrependUint8Slot(3, builtinOptionsType, 0)
def OperatorAddBuiltinOptionsType(builder, builtinOptionsType):
    """This method is deprecated. Please switch to AddBuiltinOptionsType."""
    return AddBuiltinOptionsType(builder, builtinOptionsType)
def AddBuiltinOptions(builder, builtinOptions): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(builtinOptions), 0)
def OperatorAddBuiltinOptions(builder, builtinOptions):
    """This method is deprecated. Please switch to AddBuiltinOptions."""
    return AddBuiltinOptions(builder, builtinOptions)
def AddCustomOptions(builder, customOptions): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(customOptions), 0)
def OperatorAddCustomOptions(builder, customOptions):
    """This method is deprecated. Please switch to AddCustomOptions."""
    return AddCustomOptions(builder, customOptions)
def StartCustomOptionsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def OperatorStartCustomOptionsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCustomOptionsVector(builder, numElems)
def AddCustomOptionsFormat(builder, customOptionsFormat): builder.PrependInt8Slot(6, customOptionsFormat, 0)
def OperatorAddCustomOptionsFormat(builder, customOptionsFormat):
    """This method is deprecated. Please switch to AddCustomOptionsFormat."""
    return AddCustomOptionsFormat(builder, customOptionsFormat)
def AddMutatingVariableInputs(builder, mutatingVariableInputs): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(mutatingVariableInputs), 0)
def OperatorAddMutatingVariableInputs(builder, mutatingVariableInputs):
    """This method is deprecated. Please switch to AddMutatingVariableInputs."""
    return AddMutatingVariableInputs(builder, mutatingVariableInputs)
def StartMutatingVariableInputsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def OperatorStartMutatingVariableInputsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMutatingVariableInputsVector(builder, numElems)
def AddIntermediates(builder, intermediates): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(intermediates), 0)
def OperatorAddIntermediates(builder, intermediates):
    """This method is deprecated. Please switch to AddIntermediates."""
    return AddIntermediates(builder, intermediates)
def StartIntermediatesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def OperatorStartIntermediatesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartIntermediatesVector(builder, numElems)
def End(builder): return builder.EndObject()
def OperatorEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
import tflite_.AbsOptions
import tflite_.AddNOptions
import tflite_.AddOptions
import tflite_.ArgMaxOptions
import tflite_.ArgMinOptions
import tflite_.BatchMatMulOptions
import tflite_.BatchToSpaceNDOptions
import tflite_.BidirectionalSequenceLSTMOptions
import tflite_.BidirectionalSequenceRNNOptions
import tflite_.BuiltinOptions
import tflite_.CallOptions
import tflite_.CastOptions
import tflite_.ConcatEmbeddingsOptions
import tflite_.ConcatenationOptions
import tflite_.Conv2DOptions
import tflite_.CosOptions
import tflite_.DensifyOptions
import tflite_.DepthToSpaceOptions
import tflite_.DepthwiseConv2DOptions
import tflite_.DequantizeOptions
import tflite_.DivOptions
import tflite_.EmbeddingLookupSparseOptions
import tflite_.EqualOptions
import tflite_.ExpOptions
import tflite_.ExpandDimsOptions
import tflite_.FakeQuantOptions
import tflite_.FillOptions
import tflite_.FloorDivOptions
import tflite_.FloorModOptions
import tflite_.FullyConnectedOptions
import tflite_.GatherNdOptions
import tflite_.GatherOptions
import tflite_.GreaterEqualOptions
import tflite_.GreaterOptions
import tflite_.HardSwishOptions
import tflite_.IfOptions
import tflite_.L2NormOptions
import tflite_.LSHProjectionOptions
import tflite_.LSTMOptions
import tflite_.LeakyReluOptions
import tflite_.LessEqualOptions
import tflite_.LessOptions
import tflite_.LocalResponseNormalizationOptions
import tflite_.LogSoftmaxOptions
import tflite_.LogicalAndOptions
import tflite_.LogicalNotOptions
import tflite_.LogicalOrOptions
import tflite_.MatrixDiagOptions
import tflite_.MatrixSetDiagOptions
import tflite_.MaximumMinimumOptions
import tflite_.MirrorPadOptions
import tflite_.MulOptions
import tflite_.NegOptions
import tflite_.NonMaxSuppressionV4Options
import tflite_.NonMaxSuppressionV5Options
import tflite_.NotEqualOptions
import tflite_.OneHotOptions
import tflite_.PackOptions
import tflite_.PadOptions
import tflite_.PadV2Options
import tflite_.Pool2DOptions
import tflite_.PowOptions
import tflite_.QuantizeOptions
import tflite_.RNNOptions
import tflite_.RangeOptions
import tflite_.RankOptions
import tflite_.ReducerOptions
import tflite_.ReshapeOptions
import tflite_.ResizeBilinearOptions
import tflite_.ResizeNearestNeighborOptions
import tflite_.ReverseSequenceOptions
import tflite_.ReverseV2Options
import tflite_.SVDFOptions
import tflite_.ScatterNdOptions
import tflite_.SegmentSumOptions
import tflite_.SelectOptions
import tflite_.SelectV2Options
import tflite_.SequenceRNNOptions
import tflite_.ShapeOptions
import tflite_.SkipGramOptions
import tflite_.SliceOptions
import tflite_.SoftmaxOptions
import tflite_.SpaceToBatchNDOptions
import tflite_.SpaceToDepthOptions
import tflite_.SparseToDenseOptions
import tflite_.SplitOptions
import tflite_.SplitVOptions
import tflite_.SquareOptions
import tflite_.SquaredDifferenceOptions
import tflite_.SqueezeOptions
import tflite_.StridedSliceOptions
import tflite_.SubOptions
import tflite_.TileOptions
import tflite_.TopKV2Options
import tflite_.TransposeConvOptions
import tflite_.TransposeOptions
import tflite_.UnidirectionalSequenceLSTMOptions
import tflite_.UniqueOptions
import tflite_.UnpackOptions
import tflite_.WhereOptions
import tflite_.WhileOptions
import tflite_.ZerosLikeOptions
try:
    from typing import List, Union
except:
    pass

class OperatorT(object):

    # OperatorT
    def __init__(self):
        self.opcodeIndex = 0  # type: int
        self.inputs = None  # type: List[int]
        self.outputs = None  # type: List[int]
        self.builtinOptionsType = 0  # type: int
        self.builtinOptions = None  # type: Union[None, tflite_.Conv2DOptions.Conv2DOptionsT, tflite_.DepthwiseConv2DOptions.DepthwiseConv2DOptionsT, tflite_.ConcatEmbeddingsOptions.ConcatEmbeddingsOptionsT, tflite_.LSHProjectionOptions.LSHProjectionOptionsT, tflite_.Pool2DOptions.Pool2DOptionsT, tflite_.SVDFOptions.SVDFOptionsT, tflite_.RNNOptions.RNNOptionsT, tflite_.FullyConnectedOptions.FullyConnectedOptionsT, tflite_.SoftmaxOptions.SoftmaxOptionsT, tflite_.ConcatenationOptions.ConcatenationOptionsT, tflite_.AddOptions.AddOptionsT, tflite_.L2NormOptions.L2NormOptionsT, tflite_.LocalResponseNormalizationOptions.LocalResponseNormalizationOptionsT, tflite_.LSTMOptions.LSTMOptionsT, tflite_.ResizeBilinearOptions.ResizeBilinearOptionsT, tflite_.CallOptions.CallOptionsT, tflite_.ReshapeOptions.ReshapeOptionsT, tflite_.SkipGramOptions.SkipGramOptionsT, tflite_.SpaceToDepthOptions.SpaceToDepthOptionsT, tflite_.EmbeddingLookupSparseOptions.EmbeddingLookupSparseOptionsT, tflite_.MulOptions.MulOptionsT, tflite_.PadOptions.PadOptionsT, tflite_.GatherOptions.GatherOptionsT, tflite_.BatchToSpaceNDOptions.BatchToSpaceNDOptionsT, tflite_.SpaceToBatchNDOptions.SpaceToBatchNDOptionsT, tflite_.TransposeOptions.TransposeOptionsT, tflite_.ReducerOptions.ReducerOptionsT, tflite_.SubOptions.SubOptionsT, tflite_.DivOptions.DivOptionsT, tflite_.SqueezeOptions.SqueezeOptionsT, tflite_.SequenceRNNOptions.SequenceRNNOptionsT, tflite_.StridedSliceOptions.StridedSliceOptionsT, tflite_.ExpOptions.ExpOptionsT, tflite_.TopKV2Options.TopKV2OptionsT, tflite_.SplitOptions.SplitOptionsT, tflite_.LogSoftmaxOptions.LogSoftmaxOptionsT, tflite_.CastOptions.CastOptionsT, tflite_.DequantizeOptions.DequantizeOptionsT, tflite_.MaximumMinimumOptions.MaximumMinimumOptionsT, tflite_.ArgMaxOptions.ArgMaxOptionsT, tflite_.LessOptions.LessOptionsT, tflite_.NegOptions.NegOptionsT, tflite_.PadV2Options.PadV2OptionsT, tflite_.GreaterOptions.GreaterOptionsT, tflite_.GreaterEqualOptions.GreaterEqualOptionsT, tflite_.LessEqualOptions.LessEqualOptionsT, tflite_.SelectOptions.SelectOptionsT, tflite_.SliceOptions.SliceOptionsT, tflite_.TransposeConvOptions.TransposeConvOptionsT, tflite_.SparseToDenseOptions.SparseToDenseOptionsT, tflite_.TileOptions.TileOptionsT, tflite_.ExpandDimsOptions.ExpandDimsOptionsT, tflite_.EqualOptions.EqualOptionsT, tflite_.NotEqualOptions.NotEqualOptionsT, tflite_.ShapeOptions.ShapeOptionsT, tflite_.PowOptions.PowOptionsT, tflite_.ArgMinOptions.ArgMinOptionsT, tflite_.FakeQuantOptions.FakeQuantOptionsT, tflite_.PackOptions.PackOptionsT, tflite_.LogicalOrOptions.LogicalOrOptionsT, tflite_.OneHotOptions.OneHotOptionsT, tflite_.LogicalAndOptions.LogicalAndOptionsT, tflite_.LogicalNotOptions.LogicalNotOptionsT, tflite_.UnpackOptions.UnpackOptionsT, tflite_.FloorDivOptions.FloorDivOptionsT, tflite_.SquareOptions.SquareOptionsT, tflite_.ZerosLikeOptions.ZerosLikeOptionsT, tflite_.FillOptions.FillOptionsT, tflite_.BidirectionalSequenceLSTMOptions.BidirectionalSequenceLSTMOptionsT, tflite_.BidirectionalSequenceRNNOptions.BidirectionalSequenceRNNOptionsT, tflite_.UnidirectionalSequenceLSTMOptions.UnidirectionalSequenceLSTMOptionsT, tflite_.FloorModOptions.FloorModOptionsT, tflite_.RangeOptions.RangeOptionsT, tflite_.ResizeNearestNeighborOptions.ResizeNearestNeighborOptionsT, tflite_.LeakyReluOptions.LeakyReluOptionsT, tflite_.SquaredDifferenceOptions.SquaredDifferenceOptionsT, tflite_.MirrorPadOptions.MirrorPadOptionsT, tflite_.AbsOptions.AbsOptionsT, tflite_.SplitVOptions.SplitVOptionsT, tflite_.UniqueOptions.UniqueOptionsT, tflite_.ReverseV2Options.ReverseV2OptionsT, tflite_.AddNOptions.AddNOptionsT, tflite_.GatherNdOptions.GatherNdOptionsT, tflite_.CosOptions.CosOptionsT, tflite_.WhereOptions.WhereOptionsT, tflite_.RankOptions.RankOptionsT, tflite_.ReverseSequenceOptions.ReverseSequenceOptionsT, tflite_.MatrixDiagOptions.MatrixDiagOptionsT, tflite_.QuantizeOptions.QuantizeOptionsT, tflite_.MatrixSetDiagOptions.MatrixSetDiagOptionsT, tflite_.HardSwishOptions.HardSwishOptionsT, tflite_.IfOptions.IfOptionsT, tflite_.WhileOptions.WhileOptionsT, tflite_.DepthToSpaceOptions.DepthToSpaceOptionsT, tflite_.NonMaxSuppressionV4Options.NonMaxSuppressionV4OptionsT, tflite_.NonMaxSuppressionV5Options.NonMaxSuppressionV5OptionsT, tflite_.ScatterNdOptions.ScatterNdOptionsT, tflite_.SelectV2Options.SelectV2OptionsT, tflite_.DensifyOptions.DensifyOptionsT, tflite_.SegmentSumOptions.SegmentSumOptionsT, tflite_.BatchMatMulOptions.BatchMatMulOptionsT]
        self.customOptions = None  # type: List[int]
        self.customOptionsFormat = 0  # type: int
        self.mutatingVariableInputs = None  # type: List[bool]
        self.intermediates = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        operator = Operator()
        operator.Init(buf, pos)
        return cls.InitFromObj(operator)

    @classmethod
    def InitFromObj(cls, operator):
        x = OperatorT()
        x._UnPack(operator)
        return x

    # OperatorT
    def _UnPack(self, operator):
        if operator is None:
            return
        self.opcodeIndex = operator.OpcodeIndex()
        if not operator.InputsIsNone():
            if np is None:
                self.inputs = []
                for i in range(operator.InputsLength()):
                    self.inputs.append(operator.Inputs(i))
            else:
                self.inputs = operator.InputsAsNumpy()
        if not operator.OutputsIsNone():
            if np is None:
                self.outputs = []
                for i in range(operator.OutputsLength()):
                    self.outputs.append(operator.Outputs(i))
            else:
                self.outputs = operator.OutputsAsNumpy()
        self.builtinOptionsType = operator.BuiltinOptionsType()
        self.builtinOptions = tflite_.BuiltinOptions.BuiltinOptionsCreator(self.builtinOptionsType, operator.BuiltinOptions())
        if not operator.CustomOptionsIsNone():
            if np is None:
                self.customOptions = []
                for i in range(operator.CustomOptionsLength()):
                    self.customOptions.append(operator.CustomOptions(i))
            else:
                self.customOptions = operator.CustomOptionsAsNumpy()
        self.customOptionsFormat = operator.CustomOptionsFormat()
        if not operator.MutatingVariableInputsIsNone():
            if np is None:
                self.mutatingVariableInputs = []
                for i in range(operator.MutatingVariableInputsLength()):
                    self.mutatingVariableInputs.append(operator.MutatingVariableInputs(i))
            else:
                self.mutatingVariableInputs = operator.MutatingVariableInputsAsNumpy()
        if not operator.IntermediatesIsNone():
            if np is None:
                self.intermediates = []
                for i in range(operator.IntermediatesLength()):
                    self.intermediates.append(operator.Intermediates(i))
            else:
                self.intermediates = operator.IntermediatesAsNumpy()

    # OperatorT
    def Pack(self, builder):
        if self.inputs is not None:
            if np is not None and type(self.inputs) is np.ndarray:
                inputs = builder.CreateNumpyVector(self.inputs)
            else:
                StartInputsVector(builder, len(self.inputs))
                for i in reversed(range(len(self.inputs))):
                    builder.PrependInt32(self.inputs[i])
                inputs = builder.EndVector()
        if self.outputs is not None:
            if np is not None and type(self.outputs) is np.ndarray:
                outputs = builder.CreateNumpyVector(self.outputs)
            else:
                StartOutputsVector(builder, len(self.outputs))
                for i in reversed(range(len(self.outputs))):
                    builder.PrependInt32(self.outputs[i])
                outputs = builder.EndVector()
        if self.builtinOptions is not None:
            builtinOptions = self.builtinOptions.Pack(builder)
        if self.customOptions is not None:
            if np is not None and type(self.customOptions) is np.ndarray:
                customOptions = builder.CreateNumpyVector(self.customOptions)
            else:
                StartCustomOptionsVector(builder, len(self.customOptions))
                for i in reversed(range(len(self.customOptions))):
                    builder.PrependUint8(self.customOptions[i])
                customOptions = builder.EndVector()
        if self.mutatingVariableInputs is not None:
            if np is not None and type(self.mutatingVariableInputs) is np.ndarray:
                mutatingVariableInputs = builder.CreateNumpyVector(self.mutatingVariableInputs)
            else:
                StartMutatingVariableInputsVector(builder, len(self.mutatingVariableInputs))
                for i in reversed(range(len(self.mutatingVariableInputs))):
                    builder.PrependBool(self.mutatingVariableInputs[i])
                mutatingVariableInputs = builder.EndVector()
        if self.intermediates is not None:
            if np is not None and type(self.intermediates) is np.ndarray:
                intermediates = builder.CreateNumpyVector(self.intermediates)
            else:
                StartIntermediatesVector(builder, len(self.intermediates))
                for i in reversed(range(len(self.intermediates))):
                    builder.PrependInt32(self.intermediates[i])
                intermediates = builder.EndVector()
        Start(builder)
        AddOpcodeIndex(builder, self.opcodeIndex)
        if self.inputs is not None:
            AddInputs(builder, inputs)
        if self.outputs is not None:
            AddOutputs(builder, outputs)
        AddBuiltinOptionsType(builder, self.builtinOptionsType)
        if self.builtinOptions is not None:
            AddBuiltinOptions(builder, builtinOptions)
        if self.customOptions is not None:
            AddCustomOptions(builder, customOptions)
        AddCustomOptionsFormat(builder, self.customOptionsFormat)
        if self.mutatingVariableInputs is not None:
            AddMutatingVariableInputs(builder, mutatingVariableInputs)
        if self.intermediates is not None:
            AddIntermediates(builder, intermediates)
        operator = End(builder)
        return operator
