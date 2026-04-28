import json
from pathlib import Path
import logging
from typing import List, Dict, Tuple, Union, Any
from fnmatch import fnmatch

import mkdocs
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from packaging.version import Version

from mkdocs_exclude_search.utils import explode_navigation


def get_logger():
    logger = logging.getLogger("mkdocs.plugins.mkdocs-exclude-search")
    MKDOCS_LOG_VERSION = "1.2"
    if Version(mkdocs.__version__) < Version(MKDOCS_LOG_VERSION):
        # filter doesn't do anything since that version
        # pylint: disable=import-outside-toplevel, no-name-in-module
        from mkdocs.utils import warning_filter

        logger.addFilter(warning_filter)

    return logger


logger = get_logger()


class ExcludeSearch(BasePlugin):
    """
    Excludes selected files, nav chapters and headers from the search index.
    """

    config_scheme = (
        ("exclude", config_options.Type((str, list), default=[])),
        ("ignore", config_options.Type((str, list), default=[])),
        ("exclude_unreferenced", config_options.Type(bool, default=False)),
        ("exclude_tags", config_options.Type(bool, default=False)),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def validate_config(self, plugins: List[str]):
        """
        Validate mkdocs-exclude-search plugin configuration.
        """
        pass

    @staticmethod
    def resolve_excluded_records(
        to_exclude: List[str],
    ) -> List:
        """
        Resolve the search index file-name and header-names from the user provided excluded entries.

        Args:
            to_exclude: The user provided list of excluded entries for files,
                headers and directories ("*").

        Returns:
            A list with each resolved entry as a tuple of (file-name, header-name/None).
        """
        pass

    @staticmethod
    def resolve_ignored_chapters(to_ignore: List[str]) -> List:
        """
        Supplement the search index main entry for each user provided ignored header.

        In order for a header subchapter to be available in the search index, it requires one
        "file-name" entry and one "file-name/header-name" entry.

        Args:
            to_ignore: The user provided list of ignored entries for chapters.

        Returns:
            A list with each resolved entry as a tuple of (file-name, header-name/None),
            and with the supplemented main_name entries.
        """
        pass

    @staticmethod
    def is_unreferenced_record(rec_file_name: str, navigation_items: List[str]):
        """
        Unreferenced markdown files that are not contained in mkdocs.yml navigation
        nav section.
        """
        pass

    @staticmethod
    def is_tag_record(rec_file_name: str):
        """Tags entries of mkdocs-plugin-tags"""
        pass

    @staticmethod
    def is_root_record(rec_file_name: str):
        """Required mkdocs root files.

        Collides with is_tag_record as these have no slash. Handled by order in select_included_records.
        """
        pass

    @staticmethod
    def is_ignored_record(
        rec_file_name: str, rec_header_name: Union[str, None], to_ignore: List[Tuple]
    ):
        """
        Headers selected by the user as to be ignored from the exclusions.

        Args:
            rec_file_name: The file name as in the search index record, e.g. 'all_dir/all_dir_ignore_heading1/'
            rec_header_name: The header name as in the search index record, e.g. None or
                'single-header-chapter_exclude_heading2-bbex'
            to_ignore: The list of to be ignored (records (from the exclusion) with tuples
                of (rec_file_name, rec_header_name), e.g. ('chapter_exclude_all.md', None)

        Returns:
            True if the record matches with the to_ignore list, None if not.
        """
        pass

    @staticmethod
    def is_excluded_record(
        rec_file_name: str, rec_header_name: Union[str, None], to_exclude: List[Tuple]
    ):
        """
        Files, headers or directories selected by the user to be excluded.

        Args:
            rec_file_name: The file name as in the search index record, e.g. 'chapter_exclude_all/'
            rec_header_name: The header name as in the search index record, e.g. None or
                'single-header-chapter_exclude_heading2-bbex'
            to_exclude: The list of to be excluded records with tuples of (rec_file_name, rec_header_name),
                e.g. ('chapter_exclude_all.md', None)

        Returns:
            True if the record matches with the to_exclude list, None if not.
        """
        pass

    def select_included_records(
        self,
        search_index: Dict,
        to_exclude: List[Tuple[Any, ...]],
        to_ignore: List[Tuple[Any, ...]],
        navigation_items: List[str],
        exclude_unreferenced: bool = False,
        exclude_tags: bool = False,
    ) -> List[Dict]:
        """
        Select the search index records to be included in the final selection.

        Args:
            search_index: The mkdocs search index in "config.data["site_dir"]) / "search/search_index.json"
            to_exclude: Resolved list of excluded search index records.
            to_ignore: Resolved list of ignored search index chapter records.
            navigation_items: List of markdown filepaths in the mkdocs.yml nav, in the format
                ["filename/", dir/filename/]
            exclude_unreferenced: Boolean wether unreferenced files (not listed in mkdocs nav)
                should be excluded, default False.
            exclude_tags: Boolean wether mkdocs-plugin-tags entries should be excluded, default False.

        Returns:
            A new search index as a list of dicts.
        """
        pass

    # pylint: disable=arguments-differ
    def on_post_build(self, config):
        # at mkdocs buildtime, self.config does not contain the same as config
        pass
