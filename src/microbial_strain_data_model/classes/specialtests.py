from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import TestResults
from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class SpecialTests(BaseModel):
    """Special tests that do not fit into other categories"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    dalmauPlateCulturesOnPotatoAndCornMealAgarMedia: TestResults | None = Field(
        default=None,
        description="""Dalmau plate cultures on potato and corn meal agar media.
        Controlled vocabulary: positive, negative, variable.""",
    )
    methylRed: TestResults | None = Field(
        default=None,
        description="""Methyl Red test result.
        Controlled vocabulary: positive, negative, variable.""",
    )
    vogesProskauer: TestResults | None = Field(
        default=None,
        description="""Voges-Proskauer test result.
        Controlled vocabulary: positive, negative, variable.""",
    )
    indoleTest: TestResults | None = Field(
        default=None,
        description="""Indole test result.
        Controlled vocabulary: positive, negative, variable.""",
    )
    citrateTest: TestResults | None = Field(
        default=None,
        description="""Citrate test result.
        Controlled vocabulary: positive, negative, variable.""",
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
