{{- define "pythonFlask" -}}
pythonFlask
{{- end }}

{{- define "flask-app.fullname" -}}
{{ .Release.Name }}-{{ include "flask-app.name" . }}
{{- end }}