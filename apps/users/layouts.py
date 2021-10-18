from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Column, Row, ButtonHolder


layout_user_create = Layout(
    Row(
        Column("username", css_class="mb-3"),
        Column("first_name", css_class="mb-3"),
        Column("last_name", css_class="mb-3"),
        Column("password1", css_class="mb-3"),
        Column("password2", css_class="mb-3"),
        ButtonHolder(
            Submit("submit", "Entrar", css_class="btn btn-primary w-100"),
        ),
    )
)


layout_auth = Layout(
    Row(
        Column("username", css_class="mb-3"),
        Column("password", css_class="mb-3"),
        ButtonHolder(
            Submit("submit", "Entrar", css_class="btn btn-primary w-100"),
        ),
    )
)
