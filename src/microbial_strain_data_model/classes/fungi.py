from pydantic import BaseModel, ConfigDict, Field
from enum import Enum

from microbial_strain_data_model.classes.links import SourceLink


class Fungi(BaseModel):
    """Fungi only tests"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    class MorphTypeEnum(str, Enum):
        yeast = "yeast"
        filamentous = "filamentous"

    morphType: MorphTypeEnum | None = Field(
        default=None,
        title="Morph Type",
        description="Morphological type, must be 'yeast' or 'filamentous'",
    )
    asexualReproduction: bool | None = Field(
        default=None,
        title="Asexual Reproduction",
        description="True/False for asexual reproduction",
    )
    sexualReproduction: bool | None = Field(
        default=None,
        title="Sexual Reproduction",
        description="True/False for sexual reproduction",
    )

    class TeliosporesEnum(str, Enum):
        no_teliospores = "no teliospores"
        angular = "angular"
        round_to_oval = "round to oval"
        on_hyphae_intercalary = "on hyphae intercalary"
        on_hyphae_terminal = "on hyphae terminal"
        on_hyphae_in_chains = "on hyphae in chains"

    teliospores: TeliosporesEnum | None = Field(
        default=None,
        title="Teliospores",
        description="Teliospores, controlled vocabulary",
    )
    ascospores: bool | None = Field(
        default=None, title="Ascospores", description="True/False for ascospores"
    )

    class AscosporesShapeEnum(str, Enum):
        hat_shaped = "hat shaped"
        cap_shaped = "cap shaped"
        saturn_shaped = "saturn shaped"
        walnut_shaped = "walnut shaped"
        conical = "conical"
        oblong = "oblong"
        round = "round"
        oval = "oval"
        smooth = "smooth"
        rough = "rough"
        reniform = "reniform"
        allantoid = "allantoid"
        needle_shaped = "needle shaped"
        whip_like = "whip-like"

    ascosporesShape: AscosporesShapeEnum | None = Field(
        default=None,
        title="Ascospores Shape",
        description="Shape of ascospores, controlled vocabulary",
    )
    ascosporesWithGroove: bool | None = Field(
        default=None,
        title="Ascospores With Groove",
        description="True/False if ascospores have groove",
    )
    ascosporesWithGelatinousSheath: bool | None = Field(
        default=None,
        title="Ascospores With Gelatinous Sheath",
        description="True/False if ascospores have gelatinous sheath",
    )

    class NumberRange(BaseModel):
        min: int | None = Field(default=None, title="Min", description="Minimum number")
        max: int | None = Field(default=None, title="Max", description="Maximum number")

    numberOfAscosporesPerAscus: NumberRange | None = Field(
        default=None,
        title="Number of Ascospores per Ascus",
        description="Object with number range (min/max)",
    )
    asciEvanescence: bool | None = Field(
        default=None,
        title="Asci Evanescence",
        description="True/False for asci evanescence",
    )
    clubShapedAsci: bool | None = Field(
        default=None,
        title="Club Shaped Asci",
        description="True/False for club shaped asci",
    )
    basidiospores: bool | None = Field(
        default=None, title="Basidiospores", description="True/False for basidiospores"
    )

    class BasidiaShapeEnum(str, Enum):
        clavate = "clavate"
        cylindrical = "cylindrical"
        capitate = "capitate"
        other = "other"

    basidiaShape: list[BasidiaShapeEnum] | None = Field(
        default=None,
        title="Basidia Shape",
        description="List of basidia shapes, controlled vocabulary",
    )

    class BasidiaSeptationEnum(str, Enum):
        one_celled = "one celled"
        transversely_septate = "transversely septate"
        longitudinally_obliquely_septate = "longitudinally-obliquely septate"
        other = "other"

    basidiaSeptation: BasidiaSeptationEnum | None = Field(
        default=None,
        title="Basidia Septation",
        description="Basidia septation, controlled vocabulary",
    )

    class BasidiaCatenateSolitaryEnum(str, Enum):
        no_teliospores = "no teliospores"
        angular = "angular"
        angular_and_or_no_teliospores = "angular and/or no teliospores"
        round_to_oval = "round to oval"
        round_to_oval_and_or_no_teliospores = "round to oval and/or no teliospores"
        angular_to_round_to_oval = "angular to round to oval"
        angular_to_round_to_oval_and_or_no_teliospores = (
            "angular to round to oval and/or no teliospores"
        )

    basidiaCatenateSolitary: BasidiaCatenateSolitaryEnum | None = Field(
        default=None,
        title="Basidia Catenate Solitary",
        description="Basidia catenate/solitary, controlled vocabulary",
    )

    class ConjugationTypeEnum(str, Enum):
        cell_with_cell = "cell with cell"
        cell_with_its_bud = "cell with its bud"
        bud_with_bud = "bud with bud"

    conjugation: ConjugationTypeEnum | None = Field(
        default=None,
        title="Conjugation",
        description="Type of conjugation, controlled vocabulary",
    )

    class ClampConnectionEnum(str, Enum):
        hyphae_with_no_clamp_connection = "hyphae with no clamp connection"
        hyphae_with_pseudoclamp_connection = "hyphae with pseudoclamp connection"
        hyphae_with_clamp_connection = "hyphae with clamp connection"

    clampConnection: ClampConnectionEnum | None = Field(
        default=None,
        title="Clamp Connection",
        description="Clamp connection type, controlled vocabulary",
    )

    class MatingSystemEnum(str, Enum):
        bipolar = "bipolar"
        tetrapolar = "tetrapolar"
        pseudotetrapolar = "pseudotetrapolar"
        unknown = "unknown"

    matingSystem: MatingSystemEnum | None = Field(
        default=None,
        title="Mating System",
        description="Mating system, controlled vocabulary",
    )
    complementaryMatingTypes: list[str] | None = Field(
        default=None,
        title="Complementary Mating Types",
        description="List of complementary mating types",
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
