# generated by datamodel-codegen:
#   filename:  liquid-chromatography.json
#   timestamp: 2024-01-12T14:18:37+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from allotropy.allotrope.models.shared.components.liquid_chromatography import (
    PeakList,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCentimeter,
    TQuantityValueCubicMillimeter,
    TQuantityValueHertz,
    TQuantityValueMicrometer,
    TQuantityValueMillimeter,
    TQuantityValueNanometer,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDatacube,
    TDateTimeValue,
    TQuantityValue,
    TStringValue,
)


@dataclass
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class DeviceSystemDocument:
    asset_management_identifier: TStringValue
    description: Optional[Any] = None
    brand_name: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    pump_model_number: Optional[TStringValue] = None
    detector_model_number: Optional[TStringValue] = None
    device_document: Optional[list[DeviceDocumentItem]] = None


@dataclass
class ChromatographyColumnDocument:
    chromatography_column_particle_size: Optional[TQuantityValueMicrometer] = None
    chromatography_column_chemistry_type: Optional[TStringValue] = None
    chromatography_column_serial_number: Optional[TStringValue] = None
    column_inner_diameter: Optional[TQuantityValueMillimeter] = None
    product_manufacturer: Optional[TStringValue] = None
    chromatography_column_length: Optional[TQuantityValueCentimeter] = None
    chromatography_column_part_number: Optional[TStringValue] = None


@dataclass
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    brand_name: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    detection_type: Optional[TStringValue] = None
    electronic_absorbance_wavelength_setting: Optional[TQuantityValueNanometer] = None
    electronic_absorbance_bandwidth_setting: Optional[TQuantityValueNanometer] = None
    electronic_absorbance_reference_bandwidth_setting: Optional[
        TQuantityValueNanometer
    ] = None
    electronic_absorbance_reference_wavelength_setting: Optional[
        TQuantityValueNanometer
    ] = None
    detector_offset_setting: Optional[TQuantityValue] = None
    detector_sampling_rate_setting: Optional[TQuantityValueHertz] = None
    field_index: Optional[int] = None


@dataclass
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass
class SampleDocument:
    sample_identifier: TStringValue
    description: Optional[Any] = None
    written_name: Optional[TStringValue] = None


@dataclass
class InjectionDocument:
    autosampler_injection_volume_setting__chromatography_: TQuantityValueCubicMillimeter
    injection_identifier: TStringValue
    injection_time: TDateTimeValue


@dataclass
class ProcessedDataDocument:
    peak_list: Optional[PeakList] = None


@dataclass
class DiagnosticTraceDocumentItem:
    description: Any
    data_cube: Optional[TDatacube] = None


@dataclass
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: Optional[list[DiagnosticTraceDocumentItem]] = None


@dataclass
class MeasurementDocumentItem:
    chromatography_column_document: ChromatographyColumnDocument
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    injection_document: InjectionDocument
    detection_type: TStringValue
    chromatogram_data_cube: TDatacube
    measurement_identifier: Optional[TStringValue] = None
    three_dimensional_ultraviolet_spectrum_data_cube: Optional[TDatacube] = None
    processed_data_document: Optional[ProcessedDataDocument] = None
    diagnostic_trace_aggregate_document: Optional[
        DiagnosticTraceAggregateDocument
    ] = None


@dataclass
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocumentItem]


@dataclass
class LiquidChromatographyDocumentItem:
    analyst: TStringValue
    measurement_aggregate_document: MeasurementAggregateDocument
    submitter: Optional[TStringValue] = None


@dataclass
class LiquidChromatographyAggregateDocument:
    device_system_document: DeviceSystemDocument
    liquid_chromatography_document: list[LiquidChromatographyDocumentItem]


@dataclass
class Model:
    liquid_chromatography_aggregate_document: Optional[
        LiquidChromatographyAggregateDocument
    ] = None
    manifest: str = "http://purl.allotrope.org/manifests/liquid-chromatography/REC/2023/03/liquid-chromatography.manifest"
