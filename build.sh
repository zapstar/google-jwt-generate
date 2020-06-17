#!/usr/bin/env bash
set -ex
TEMP_DIR="${PWD}/tmp"
INSTALLER_FILE="gen-id-token.pyz"
TEMP_INSTALLER_FILE="${TEMP_DIR}/${INSTALLER_FILE}"
mkdir -p "${TEMP_DIR}"
function cleanup {
  rm -r "${TEMP_DIR}"
}
trap cleanup EXIT
# Install all packages for Python2, works with Python3 as well.
pipenv lock -r > "${TEMP_DIR}/requirements.txt"
PYTHONWARNINGS=ignore:DEPRECATION pip2 install --no-compile --no-cache --ignore-installed --requirement "${TEMP_DIR}/requirements.txt" --target "${TEMP_DIR}/"
touch "${TEMP_DIR}/google/__init__.py"
find "${TEMP_DIR}" -name '*.dist-info' | xargs rm -r
cp __main__.py "${TEMP_DIR}/"
(cd "${TEMP_DIR}" && zip -x "bin/*" -x "requirements.txt" -r -9 "${TEMP_INSTALLER_FILE}" *)
echo "#!/usr/bin/env python" | cat - "${TEMP_INSTALLER_FILE}" > "${INSTALLER_FILE}"
chmod +x "${INSTALLER_FILE}"
