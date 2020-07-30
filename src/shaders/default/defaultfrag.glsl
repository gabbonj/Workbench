#version 330 core
out vec4 FragColor;

in vec2 TexCoord;

uniform sampler2D ourTexture;

vec4 data;

void main()
{
    data = texture(ourTexture, TexCoord);
    FragColor = vec4(data.x, data.y, data.z, 1.0);
}