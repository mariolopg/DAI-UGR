import BlogPreview from "./BlogPreview";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

const BlogList = ({blogs, title, handleDelete}) => {
    return (
        <div className="blog-list">
            <h2>{ title }</h2>
            <Container>
                <Row>
                    {blogs.map((blog) => (
                        <BlogPreview blog = { blog } handleDelete = { handleDelete } key = { blog.id } />
                    ))}
                </Row>
            </Container>
            
        </div>
    );
}
 
export default BlogList;