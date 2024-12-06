import re
import sys
from pathlib import Path

from django.conf import settings
from django_translate_gettext.exceptions import TranslatorError

from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException


class PoFileMultiLineTranslator:
	def __init__(self, lang_code: str):
		self.lang_code = lang_code
		# self.locale_paths = [Path(filepath) for filepath in settings.LOCALE_PATHS]
		try:
			self.translator = GoogleTranslator(source="auto", target=lang_code)
		except LanguageNotSupportedException as error:
			raise TranslatorError(f"Language code {lang_code} is not supported by the translator") from error

	def translate_block(self, block: str, msgid: list[str]) -> str:
		msgstr = re.findall(r'msgstr "(.*?)"', block)
		if msgstr and msgstr[0]:
			return block
		translated = self.translator.translate(msgid[0])
		return re.sub(r'msgstr "(.*?)*"', f'msgstr "{translated}"', block)

	def process_first_block(self, block: str) -> str:
		parts = block.split("\n")
		raw_msgid, raw_msgstr = parts[-2], parts[-1]
		msgid = re.findall(r'msgid "(.*?)"', raw_msgid)
		parts[-1] = self.translate_block(block=raw_msgstr, msgid=msgid)
		return "\n".join(parts)
	
	def process_multi_line_block(self, block: str) -> str:
		...

	def translate_locale_path(self, *, locale_path: Path) -> None:
		result = []
		# po_file = locale_path.joinpath(self.lang_code, "LC_MESSAGES", "django.po")
		po_file = locale_path
		if not po_file.exists():
			raise TranslatorError(f"The file for code {self.lang_code} does not exist.")

		file_content = po_file.read_text().split("\n\n")
		for block in file_content:
			if not block:
				continue

			msgid = re.findall(r'msgid "(.*?)"', block)
			if len(msgid) != 1:
				result.append(self.process_first_block(block=block))
				continue

			result.append(self.translate_block(block=block, msgid=msgid))

		po_file.write_text("\n\n".join(result))

	def translate_codes(self) -> None:
		try:
		# for locale_path in self.locale_paths:
			self.translate_locale_path(locale_path=Path(sys.argv[1]))
		except IndexError as e:
			print('Path name required.')
			exit(1)



t = PoFileMultiLineTranslator('de')
t.translate_codes()
