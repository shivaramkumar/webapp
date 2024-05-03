from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import DEV_DEPENDENCIES
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent
from ambient_package_update.metadata.ruff_ignored_inspection import RuffIgnoredInspection

METADATA = PackageMetadata(
    package_name='shivarams_blog',
    authors=[
        PackageAuthor(
            name='Shivaram Kumar',
            email='connect.shivaram@gmail.com',
        ),
    ],
    development_status='5 - Production/Stable',
    readme_content=ReadmeContent(
        tagline="Shivaram's Blogspace",
        content="""Contains basic blog posts and articles on various topics.
""",
    ),
    dependencies=[
        'django>=5.0',
    ],
    optional_dependencies={
        'dev': [
            *DEV_DEPENDENCIES,
        ],
        # you might add further extras here
    },
    ruff_ignore_list=[
        RuffIgnoredInspection(key='XYZ', comment="Reason why we need this exception"),

    ],
)